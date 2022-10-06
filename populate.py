import os
from string import digits
os.environ.setdefault('DJANGO_SETTINGS_MODULE','office_emp_proj.settings')

import django
django.setup()

import random
from emp_app.models import Department,Role,Employee
from faker import Faker

obj = Faker()
countries = ['Bangalore','Hyderabad','Mumbai','Chennai','Noida', 'Gurgaon']
roles = ['Product Manager','Information Architect','Software Developer','Software Project Manager','Data Scientist','Web Developer']
dept_name = ['Design', 'Software', 'Web Development', 'Marketing','Social Media']

def add_role():
    t=Role.objects.get_or_create(name = random.choice(roles))[0]
    t.save()
    return t


def call(N=5):
    for i in range(N):
        full_name = obj.name()
        list =full_name.split() 
        first_name = list[0]
        last_name = list[1]
        salary =  obj.random_number(digits=6)
        bonus = obj.random_number(digits=4)
        role = add_role()
        phone = obj.random_number(digits=10)
        hire_date = obj.date()
        location = obj.random.choice(countries)
        name = obj.random.choice(dept_name)

        dept= Department.objects.get_or_create(name =  name, location = location)[0]
        emp = Employee.objects.get_or_create(first_name = first_name , last_name = last_name , dept = dept ,salary = salary, bonus = bonus, role = role , phone = phone,hire_date= hire_date)[0]


if __name__ == '__main__':
    print("Populating script")
    call(10)
    print("Populating complete")