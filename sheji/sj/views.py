from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse

# Create your views here.
from .models import User
def index(request):
  return render(request,'sj/index.html')

def xuanze(request):
  return render(request,'sj/xuanze.html')

def wode(request):
  return render(request, 'sj/wode.html')

def login(request):
  if request.method=='GET':
    return render(request,'sj/login.html')
  else:
    if request.is_ajax():
      phonetell = request.POST.get('phonetell', None)
      password = request.POST.get('password', None)
      result=User.objects.all()
      for k in result:
        print(phonetell, k.phonetell, password, k.password)
        if str(phonetell)== str(k.phonetell) and str(password)== str(k.password):
          return JsonResponse({'statu':'ok'})
        else:
          return JsonResponse({'statu':'error'})
    else:
      return render(request, 'sj/login.html')

def phonetell(request):
  if request.method == 'GET':
    return render(request, 'sj/login.html')
  else:
    if request.is_ajax():
      phonetell = request.POST.get('phonetell', None)
      result = User.objects.all()
      for i in result:
        if str(phonetell)== str(i.phonetell) :
          return JsonResponse({'statu':'phzq'})
        else:
          return JsonResponse({'statu':'phcw'})
def password(request):
  if request.method == 'GET':
    return render(request, 'sj/login.html')
  else:
    if request.is_ajax():
      password = request.POST.get('password', None)
      result = User.objects.all()
      for i in result:
        if str(password)== str(i.password) :
          return JsonResponse({'statu':'pazq'})
        else:
          return JsonResponse({'statu':'pacw'})


def reg(request):
  if request.method == 'GET':
    return render(request, 'sj/reg.html')
  else:
    if request.method == 'POST':
      phonetell = request.POST.get('phonetell', None)
      password=request.POST.get('password', None)
      obj=User(phonetell=phonetell,password=password)
      obj.save()
      return redirect(reverse('sj:login'))
    else:
      return render(request, 'sj/reg.html')

def shouye(request):
  return render(request,'sj/shouye.html')

def shouyexx(request):
  return render(request,'sj/shouyexx.html')

def index0(request):
  return render(request,'sj/index0.html')

def index2(request):
  return render(request,'sj/index2.html')

def foster_care(request):
  return render(request,'sj/foster_care.html')

def fabu(request):
  return render(request,'sj/fabu.html')

def send_pet(request):
  return render(request,'sj/send_pet.html')

def mine(request):
  return render(request,'sj/mine.html')

def add_pet(request):
  return render(request,'sj/add_pet.html')

def Pet_species(request):
  return render(request,'sj/Pet_species.html')

def issue(request):
  return render(request,'sj/issue.html')

def personal_dynamics(request):
  return render(request,'sj/personal_dynamics.html')

def personal_information(request):
  return render(request,'sj/personal_information.html')

def dynamic_details(request):
  return render(request,'sj/dynamic_details.html')

def position(request):
  return render(request,'sj/position.html')

def pet_details(request):
  return render(request,'sj/pet_details.html')

def my_pet(request):
  return render(request,'sj/my_pet.html')

def species_con(request):
  return render(request,'sj/species_con.html')

def Type_details(request):
  return render(request,'sj/Type_details.html')
