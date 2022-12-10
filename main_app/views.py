from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Car, Accessory
from .forms import ServiceForm

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class CarCreate(LoginRequiredMixin, CreateView):
  model = Car
  fields = ['make', 'model', 'year', 'color', 'kms', 'trans']

  def form_valid(self, form):
    form.instance.user = self.request.user   
    return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  fields = '__all__'

class CarDelete(LoginRequiredMixin, DeleteView):
  model = Car
  success_url = '/cars/'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars })

@login_required
def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  accessories_car_doesnt_have = Accessory.objects.exclude(id__in = car.accessories.all().values_list('id'))
  service_form = ServiceForm()
  return render(request, 'cars/detail.html', { 
    'car': car, 'service_form': service_form, 'accessories': accessories_car_doesnt_have })

@login_required
def assoc_accessory(request, car_id, accessory_id):
  Car.objects.get(id=car_id).accessories.add(accessory_id)
  return redirect('detail', car_id=car_id)

@login_required
def unassoc_accessory(request, car_id, accessory_id):
  Car.objects.get(id=car_id).accessories.remove(accessory_id)
  return redirect('detail', car_id=car_id)

@login_required
def add_service(request, car_id):
  form = ServiceForm(request.POST)
  if form.is_valid():
    new_service = form.save(commit=False)
    new_service.car_id = car_id
    new_service.save()
    return redirect('detail', car_id=car_id)

class AccessoryList(LoginRequiredMixin, ListView):
  model = Accessory

class AccessoryDetail(LoginRequiredMixin, DetailView):
  model = Accessory

class AccessoryCreate(LoginRequiredMixin, CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(LoginRequiredMixin, DeleteView):
  model = Accessory
  success_url = '/accessories/'