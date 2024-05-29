from django.shortcuts import redirect,render, get_object_or_404
from .models import Question, Choice

# Create your views here.

from django.http import HttpResponse
from django.http import Http404

def home(request):
    questions = Question.objects.all()
    return render(request, 'polls/home.html',{
        "questions": questions
    })
def vote(request, q_id):
    question = get_object_or_404(Question, id=q_id)
    if request.method == 'POST':
     try: 
        choice = request.POST['choice']
        c = Choice.objects.get(id=choice)
        c.votes +=1
        c.save()
        return redirect('polls:results', q_id)
     except (KeyError) :
        return render(request,'polls/question.html',{
           "question": question,
           "error_message": "No elegiste ninguna opcion"
        })
    return render(request,'polls/question.html',{
        "question": question,
     })

def results(request, q_id):
    question = get_object_or_404(Question, id=q_id)
    choices = question.choice_set.all()  # 
    labels = [choice.choice_text for choice in choices]
    votes = [choice.votes for choice in choices]

    data = {
        'labels': labels,
        'datasets': [{
            'label': 'Votes',
            'data': votes,
            'backgroundColor': [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            'borderColor': [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            'borderWidth': 1
        }]
    }

    return render(request, 'polls/results.html', {
        'question': question,
        'data': data
    })
