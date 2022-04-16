
from unicodedata import name
from django.urls import path

from .views import About, Add_Appointment, Add_Patient, Contact, Delete_Appointment, Delete_Doctor, Delete_Patient, Home, Login, Logout_admin, Index, View_Appointment, View_Doctor, Add_Doctor, View_Patient


urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='admin_login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),

    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),
    path('delete_doctor(?p<int:pid>)/', Delete_Doctor, name='delete_doctor'),
    path('delete_patient(?p<int:pid>)/', Delete_Patient, name='delete_patient'),
    path('delete_appointment(?p<int:pid>)/', Delete_Appointment, name='delete_appointment'),

]