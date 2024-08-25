from django.shortcuts import render
from .models import *
from django.db.models import F, Value, Count
from django.db.models.functions import Concat
from django.utils.dateformat import DateFormat
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
import json


# Create your views here.

class EmployeeView(View):
    template_name = "employee.html"

    def get(self, request):
        employees = Employee.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name')).order_by('hire_date')

        employees_count = employees.count()

        return render(request, self.template_name, {"employees": employees, "employees_count": employees_count})

class PositionView(View):
    template_name = "position.html"

    def get(self, request):
        positions = Position.objects.values('id', 'name').order_by('id').annotate(
            position_count=Count('employee')
        )

        return render(request, self.template_name, {"positions": positions})

class ProjectView(View):
    template_name = "project.html"
    def get(self, request):
        projects = Project.objects.values('id', 'name', 'due_date', 'start_date').order_by('id')

        return render(request, self.template_name, {"projects": projects})

    def delete(self, request, **kwargs):
        data = json.loads(request.body)
        pro_id = data.get('pro_id')
        project = Project.objects.get(id=pro_id)
        project.delete()
        return JsonResponse({'success': True})

class ProjectDetailView(View):
    template_name = "project_detail.html"

    def get(self, request, **kwargs):

        id = self.kwargs.get('id')

        project_detail = Project.objects.get(id=id)

        formatted_start_date = project_detail.start_date.strftime('%Y-%m-%d')
        formatted_due_date = project_detail.due_date.strftime('%Y-%m-%d')

        project_manager = project_detail.manager.first_name + " " + project_detail.manager.last_name

        other_managers = Employee.objects.annotate(full_name=Concat(F('first_name'), Value(' '), F('last_name'))).values('id', 'full_name')

        staffs = project_detail.staff.all()

        context = {
            'project_id': project_detail.id,
            'name': project_detail.name,
            'description': project_detail.description,
            'start_date': formatted_start_date,
            'due_date': formatted_due_date,
            'manager_id': project_detail.manager.id,
            'project_manager': project_manager,
            'staffs': staffs,
            'other_managers': other_managers,
        }

        return render(request, self.template_name, context)

    def put(self, request, **kwargs):
        id = self.kwargs.get('id')
        data = json.loads(request.body)
        project = Project.objects.get(id=id)
        employee = Employee.objects.get(id=data.get('emp_id'))
        project.staff.add(employee)
        return JsonResponse({'success': True})

    def delete(self, request, **kwargs):
        id = self.kwargs.get('id')
        data = json.loads(request.body)
        emp_id = data.get('emp_id')
        project = Project.objects.get(id=id)
        employee = Employee.objects.get(id=emp_id)
        project.staff.remove(employee)
        return JsonResponse({'success': True})
