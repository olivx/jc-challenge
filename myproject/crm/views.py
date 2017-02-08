# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy as r
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, DeleteView
from .mixins import CounterMixin
from .models import Company
from .forms import CompanyForm


class CompanyList(CounterMixin, ListView):
    model = Company
    paginate_by = 10

    def get_queryset(self):
        companies = Company.objects.all()
        q = self.request.GET.get('search_box')
        if q is not None:
            companies = companies.filter(name__icontains=q)
        return companies


def company_create_form(request, form, template_name):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            companies = Company.objects.all()
            data['html_company_list'] = render_to_string(
                'includes/partial_company_list.html', {'company_list': companies})
            data['is_form_valid'] = True
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
    return company_create_form(request, form, 'crm/company_form.html')


company_detail = DetailView.as_view(model=Company)

company_delete = DeleteView.as_view(
    model=Company, success_url=r('crm:company_list'))
