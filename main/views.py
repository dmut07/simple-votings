import datetime
from django.contrib.auth import authenticate, login

from django.core.handlers.wsgi import WSGIRequest
# from main.forms import HomeForm
from django.shortcuts import render

from django.contrib.auth import authenticate
from django.shortcuts import redirect

from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from simple_votings.forms import UserForm, LoginForm, VotingForm
from main.models import Profile, Vote, Option


def index_page(request: WSGIRequest):
    context = {}
    return render(request, 'pages/index.html', context)


def time_page(request: WSGIRequest):
    context = {
        'time': datetime.datetime.now().time(),
    }
    return render(request, 'pages/time.html', context)


def votes(request):
    context = {
            'votes': Vote.objects.all(),
        }
    context['user_id'] = get_user_id(request)
    return render(request, 'pages/votes.html', context)

def get_user_id(request):
    if auth.get_user(request).id:
        return int(auth.get_user(request).id)
    else:
        return 0

def registration_page(request):
    context = {}
    context['user_id'] = get_user_id(request)
    context['error'] = ''
    if auth.get_user(request).is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
                user1 = User.objects.filter(username=form.data["username"])
                if not user1:
                    user = User(username=form.data["username"])
                    user.set_password(form.data['password'])
                    user.save()
                    new_profile = Profile(user=user)
                    new_profile.save()
                    return redirect('/')
                else:
                    context["error"] = "Username is already taken"
        context["form"] = form
    else:
        context['form'] = UserForm(request.POST)
    return render(request, 'registration/registration.html', context)


def login_page(request: WSGIRequest):
    context = {}
    context['error'] = ''
    context['user_id'] = get_user_id(request)
    if request.method == "GET":
        form = LoginForm()
        context['form'] = form
        if auth.get_user(request).is_authenticated:
            return redirect('/')

    if request.method == "POST":
        if auth.get_user(request).is_authenticated:
            return redirect('/')
        form = LoginForm(request.POST)
        context['form'] = form
        if form.is_valid():
            user = authenticate(username=form.data["username"], password=form.data["password"])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                context['error'] = 'wrong password'
                return render(request, "registration/login.html", context)
        else:
            return redirect('/login')

    return render(request, "registration/login.html", context)


def vote_create_page(request: WSGIRequest):
    context = {}
    context['user_id'] = get_user_id(request)
    if request.method == "POST":
        form = VotingForm(request.POST)
        if form.is_valid():
            vote = Vote(title=form.data["title"], description=form.data["text"])
            vote.user_id = int(auth.get_user(request).id)
            vote.user_name = auth.get_user(request).username
            vote.save()
            context["title"] = form.data["title"]
            context["text"] = form.data["text"]
            context["form"] = form
            context["votes"] = Vote.objects.all()
            redirect('vote/' + str(vote.user_id))
            return redirect('/votes/')
        else:
            context["form"] = form
    else:
        context["form"] = VotingForm()
    return render(request, 'pages/create_vote.html', context)


def voting_page(request, _id):
    vote = Vote.objects.get(id=_id)
    context = {
        'title': vote.title,
        'description': vote.description,
        'question': {
            "name": vote.title,
            "ques": [
                {
                    "id": "1",
                    "text": "I agree",
                },
                {
                    "id": "2",
                    "text": "I disagree",
                },
            ],
        },
    }
    return render(request, "pages/vote.html", context)
