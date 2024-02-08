from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Usuario
from .forms import NameForm


def all_user():
    return Usuario.objects.all()

def filter_user():
    return Usuario.objects

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            user = Usuario.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            user.save()
            return HttpResponseRedirect('/view')
    else:        
        form = NameForm()

    return render(request, "form.html", {'form': form})
    

def view_name(request):
    users = all_user()
    return render(request, "visualizar_user.html", {'users':users})    

def delete_user(request, user_id):
    user = Usuario.objects.get(id=user_id)

    user.delete()

    return HttpResponseRedirect('/view')
