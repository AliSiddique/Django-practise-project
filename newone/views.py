from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import Lead, User
import datetime
from django.contrib import messages
from .forms import LeadForm, NewForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def first(request):
    return HttpResponse("hjo")


class LeadList(LoginRequiredMixin, ListView):
    template_name = 'newone/Lead.html'
    context_object_name = 'Leads'        

    def get_queryset(self):
     return Lead.objects.filter(user=self.request.user)
         

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'newone/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        total = Lead.objects.filter(user=self.request.user).count()
        dates = Lead.objects.filter(user=self.request.user, name='more lead').count()

        context.update({
            'total': total,
            'dates':dates
        })
        return context





class LeadDetail(DetailView):
    template_name = 'newone/leaddetail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'



class LeadCreate(LoginRequiredMixin,CreateView):
    form_class = LeadForm
    template_name = 'newone/leadcreate.html'
   

    def get_success_url(self):
        return reverse("list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Created a new lead hahah")
        return super(LeadCreate, self).form_valid(form)    
        


class LeadUpdate(UpdateView):
    form_class = LeadForm
    template_name = 'newone/leadupdate.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("list")


class Signup(CreateView):
    template_name = 'newone/registration/signup.html'
    form_class = NewForm


    def get_success_url(self):
        return reverse("list")


class Login(LoginView):
    template_name = 'newone/registration/login.html'




    def get_success_url(self):
        return reverse("list")


class LogOut(LogoutView):
    template_name = 'newone/Lead.html'



    def get_success_url(self):
        return reverse("list")        