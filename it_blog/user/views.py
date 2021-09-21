from django.http import request
from django.shortcuts import render
from user.forms import UserSignIn



def signin(request):
    print(request.POST)
    context = {
        "signin_form": UserSignIn()
    }
    return render(request, "sign_in.html", context)