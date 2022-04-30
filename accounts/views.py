from django.shortcuts import render, redirect,HttpResponseRedirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login

#
# def home(request):
#     return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            #
            # user = authenticate(username=username, password=password)
            login(request, user) #

        return redirect('/')

    else:
        form = SignupForm()
        return render(request, 'registration/signup.html', {"form": form})
