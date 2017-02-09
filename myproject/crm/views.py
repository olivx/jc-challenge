# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView
from .models import Company
from .forms import CompanyForm


class CompanyList(ListView):
    model = Company
    paginate_by = 10


def company_create_form(request, form, template_name):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            companies = Company.objects.all()
            print(companies)
            data['is_form_valid'] = True
            data['html_company_list'] = render_to_string(template_name='crm/company_table.html',
                                                         context={'object_list': companies}, request=request)
        else:
            data['is_form_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)

    return JsonResponse(data)


def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
    else:
        form = CompanyForm()
    return company_create_form(request, form, 'crm/company_create_form.html')


def company_update(request, uuid):
    company = get_object_or_404(Company, pk_uuid=uuid)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
    else:
        form = CompanyForm(instance=company)
    return company_create_form(request, form, 'crm/company_update_form.html')


def company_delete(request, uuid):
    data = {}
    company = get_object_or_404(Company, pk_uuid=uuid)
    if request.method == 'POST':
        company.delete()
        companies = Company.objects.all()
        data['is_form_valid'] = True
        data['html_company_list'] = render_to_string(template_name='crm/company_table.html',
                                                     context={'object_list': companies}, request=request)

    else:
        context = {
            'company_name':company.name,
            'form': CompanyForm(instance=company)
        }
        data['html_form'] = render_to_string(
            template_name='crm/company_delete_form.html', context=context, request=request)


    return JsonResponse(data)
