from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('all/',views.all_emp, name= 'all_emp'),
    path('add/',views.add_emp, name= 'add_emp'),
    path('remove/',views.remove_emp, name= 'remove_emp'),
    path('remove/<int:emp_id>',views.remove_emp, name= 'remove_emp'),
    path('filter_emp/',views.filter_emp, name= 'filter_emp'),

]
