from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Usuario
from .forms import NameForm

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
            return HttpResponseRedirect('/thanks/')
    else:        
        form = NameForm()

    return render(request, "form.html", {'form': form})
    
