from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from . import models
from . import forms


@login_required(login_url='login')
def profile(request):
    return render(request, 'main/profile.html')


@login_required(login_url='login')
def create(request):

    if request.method == 'POST':
        form = forms.FilmCreationForm(request.POST, request.FILES)

        if form.is_valid():
            film = form.save(commit=False)
            film.owner = request.user  # User
            film.save()
            return redirect('home')
        else:
            return redirect('create_film')

    form = forms.FilmCreationForm()
    context = {
        'form': form,
        'btn_text': 'Create film',
        'btn_color': 'success',
    }
    return render(request, 'main/film_form.html', context)


def index(request):
    films = models.Film.objects.all()  # SELECT * FROM Film

    context = {
        'films': films,
    }
    return render(request, 'main/index.html', context)


def detail(request, pk):
    film = models.Film.objects.get(id=pk)

    context = {
        'film': film
    }
    return render(request, 'main/detail.html', context)


@login_required(login_url='login')
def delete(request, pk):
    film = models.Film.objects.get(id=pk)

    if request.method == 'POST':
        if film.owner == request.user:
            film.delete()
            return redirect('home')

    context = {
        'film': film,
    }
    return render(request, 'main/delete.html', context)


@login_required(login_url='login')
def edit(request, pk):
    film = models.Film.objects.get(id=pk)

    if film.owner != request.user:
        return redirect('home')

    if request.method == 'POST':
        form = forms.FilmCreationForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('edit', pk=pk)

    form = forms.FilmCreationForm(instance=film)
    context = {
        'form': form,
        'btn_text': 'Update film',
        'btn_color': 'warning'
    }
    return render(request, 'main/film_form.html', context)


def signin(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # validate username and password and let the user log in to the system
        username = request.POST.get('username')
        password = request.POST.get('password')

        '''
        authenticate(username="...", password="...") --> returns None if a user with those 
                                                        credentials not found or returns a real user
                                                         object we cn work with if a user with those 
                                                         credential found in a database
        '''
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    context = {}
    return render(request, 'main/signin.html', context)


def signup(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')

    else:
        form = forms.UserRegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'main/signup.html', context)


def signout(request):
    logout(request)
    return redirect('login')

