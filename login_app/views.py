from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from login_app.forms import LoginForm


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        else:
            return render(request, 'login_incorrect.html', {"username": username, "message": "Logowanie nieudane"})
        return render(request, 'login_correct.html', {'username': username})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))
