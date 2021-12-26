from django.shortcuts import render
from django.views import View
from requests import request

login_page = "accounts/login.html"
class Login(View):
    def get(self,request):
        return render(request, login_page)

    def post(self):
        return ""