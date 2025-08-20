from django.shortcuts import render,redirect
from .forms import Empforms
from .models import Employee
from django.db.models import Sum, Count

# Create your views here.
def add(request):
    empforms=Empforms()
    return render (request,'add.html',{'empforms':empforms})

def insert(request):
     if request.method=="POST":
         empforms=Empforms(request.POST)
         if empforms.is_valid():
             empforms.save()
             return redirect('show')
         else:
             return redirect('add')

def show(request):
    employee=Employee.objects.all()

    # --- ADD THESE LINES ---
    # Calculate Total Employees
    total_employees = employee.count()

    # Calculate Total Salary
    total_salary_data = employee.aggregate(total_salary=Sum('salary'))
    total_salary = total_salary_data.get('total_salary', 0) or 0 

    context = {
        'employee': employee,
        'total_employees': total_employees,
        'total_salary': total_salary,
    }
    return render(request,'show.html', context) # <-- Modify this line to pass 'context'
    
def edit(request,eid):
  emp=Employee.objects.get(eid=eid)
  return render(request,'edit.html',{'emp':emp})

def update(request,eid):
    if request.method=='POST':
        emp=Employee.objects.get(eid=eid)
        form=Empforms(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('show')
        else:
            return render(request,'edit.html',{'emp':emp})

def delete(request,eid):
    emp=Employee.objects.get(eid=eid)
    emp.delete()
    return redirect('show')