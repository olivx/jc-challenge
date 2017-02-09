from django.conf.urls import include, url
from myproject.crm import views as c

company_patterns = [
    url(r'^$', c.CompanyList.as_view(), name='company_list'),
    url(r'^add/$', c.company_create, name='company_add'),
    url(r'^update/(?P<uuid>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$',c.company_update, name='company_update'),
    url(r'^delete/(?P<uuid>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$',c.company_delete, name='company_delete'),
    # url(r'^d/(?P<uuid>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/detail/$',c.company_details, name='company_details'),

    # url(r'^(?P<pk>\d+)/$', c.company_detail, name='company_detail'),
    # url(r'^(?P<pk>\d+)/delete/$', c.company_delete, name='company_delete'),
]

urlpatterns = [
    url(r'^company/', include(company_patterns)),
]
