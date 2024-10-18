from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from accounts.forms import UserRejistrationForm
from django.contrib.auth import login
from django.urls import reverse_lazy


# Create your views here.

class UserRejistrationView(FormView):
    template_name='accounts/UserRejistration.html'
    form_class= UserRejistrationForm
    success_url=reverse_lazy('SignupPage')

    def form_valid(self,form):
        user=form.save()
        login(user)
        return super.form_valid(form)
        
