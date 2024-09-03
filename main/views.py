from django.shortcuts import render,redirect,get_object_or_404
from .models import Question, Choice, Vote
from .forms import VoteForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def home_view(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions': questions})


#details views
def detail_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

#results views
def results_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choices.all()  
    return render(request, 'results.html', {'question': question, 'choices': choices})
#vote views

def vote_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = VoteForm(question, request.POST)
        if form.is_valid():
            selected_choice = form.cleaned_data['choice']
            # Check if the user has already voted for this question
            if not Vote.objects.filter(user=request.user, choice__question=question).exists():
                # Create a vote and increment the choice's vote count
                vote = Vote(user=request.user, choice=selected_choice)
                vote.save()
                selected_choice.votes += 1
                selected_choice.save()
            return redirect('results', question_id=question.id)
    else:
        form = VoteForm(question)
    
    return render(request, 'detail.html', {'question': question, 'form': form})