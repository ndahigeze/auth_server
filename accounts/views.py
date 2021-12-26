from django.contrib import messages, redirects
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from requests import request

from accounts.forms import LoginForm
from accounts.models import User

login_page = "accounts/login.html"
class Login(View):
    def get(self,request):
        return render(request, login_page)

    def post(self,request):
        try:
            form = LoginForm(request.POST)
            if form.is_valid():
                user = User.find_by_email(request.POST['email'])
                if user is not None:
                    if User.check_password(user, request.POST["password"]):
                        login(request,user)
                        return redirect("accounts:login")
                    else:
                        messages.error(request,
                                       "invalid credentials, Wrong email or password")
                        return render(request, login_page)
                else:
                    messages.error(request,
                                   "invalid credentials, Wrong email or password")
                    return render(request, login_page)
            else:

                messages.error(request,
                               "invalid credentials, Wrong email or password")
                return render(request, login_page)

        except Exception as e:
            print(str(e))
            messages.error(request,
                           "invalid credentials, Wrong email or password")
            return render(request, login_page)


