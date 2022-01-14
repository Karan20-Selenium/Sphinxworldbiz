from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from app.forms import CustomerRegistrationForm,ProjectRegistrationForm  
from .models import Project,User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

def login(request):
 return render(request, 'app/login.html')

class customerregistrationView(View):

  def get(self,request):

    form = CustomerRegistrationForm()

    return render(request, 'app/customerregistration.html',{'form':form})

  def post(self,request):

    form = CustomerRegistrationForm(request.POST)

    if form.is_valid():
      form.save()
      messages.success(request, 'Congratulations!! Registered Successfully')

    return render(request,'app/customerregistration.html',{'form':form})


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):

  template_name = 'app/profile.html'
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    fm = ProjectRegistrationForm()
    projects = Project.objects.all()
    users = User.objects.all()
    context = {'projects':projects, 'form':fm, 'users':users}
    return context
  
  def post(self, request):

    form = ProjectRegistrationForm(request.POST)
    if form.is_valid():
      usr = request.user
      project = form.cleaned_data['project']
      reg = Project(project = project, user=request.user)
      reg.save()

      messages.success(request, 'Congratulations!! Project Updated Successfully')
      form = ProjectRegistrationForm()
      

    return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})  


# This Class will Update/Edit
@method_decorator(login_required, name='dispatch')
class ProjectUpdateView(View):

  def get(self, request, id):
    pi = Project.objects.get(pk=id)
    fm = ProjectRegistrationForm(instance=pi)
    return render(request, 'app/updateproject.html', {'form':fm})
  
  def post(self, request, id):
    pi = Project.objects.get(pk=id)
    fm = ProjectRegistrationForm(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
    return HttpResponseRedirect('/')

# This Class will Delete
@method_decorator(login_required, name='dispatch')
class ProjectDeleteView(RedirectView):
  url = '/'
  def get_redirect_url(self, *args, **kwargs):
    del_id = kwargs['id']
    Project.objects.get(pk=del_id).delete()
    return super().get_redirect_url(*args, **kwargs)


