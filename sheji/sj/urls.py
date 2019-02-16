from django.contrib import admin
from django.urls import path,include
from . import views
app_name='sj'
urlpatterns = [
    path('', views.index,name='index'),
    path('xuanze/', views.xuanze,name='xuanze'),
    path('login/', views.login,name='login'),
    path('reg/', views.reg,name='reg'),
    path('wode/', views.wode,name='wode'),
    path('phonetell/', views.phonetell,name='phonetell'),
    path('password/', views.password,name='password'),
    path('shouye/', views.shouye,name='shouye'),
    path('shouyexx/', views.shouyexx,name='shouyexx'),
    path('index0/', views.index0, name='index0'),
    path('index2/', views.index2, name='index2'),
    path('foster_care/', views.foster_care, name='foster_care'),
    path('fabu/', views.fabu, name='fabu'),
    path('send_pet/', views.send_pet, name='send_pet'),
    path('mine/', views.mine, name='mine'),
    path('add_pet/', views.add_pet, name='add_pet'),
    path('Pet_species/', views.Pet_species, name='Pet_species'),
    path('issue/', views.issue, name='issue'),
    path('personal_dynamics/', views.personal_dynamics, name='personal_dynamics'),
    path('personal_information/', views.personal_information, name='personal_information'),
    path('dynamic_details/', views.dynamic_details, name='dynamic_details'),
    path('position/', views.position, name='position'),
    path('pet_details/', views.pet_details, name='pet_details'),
    path('my_pet/', views.my_pet, name='my_pet'),
    path('species_con/', views.species_con, name='species_con'),
    path('Type_details/', views.Type_details, name='Type_details'),
]
