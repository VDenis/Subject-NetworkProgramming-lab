# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from models import Professor, Student, Subject, Group, PageLaboratoryWork, MadeLaboratoryWork, LabComment
from lab.views import StudentListView, ProfessorListView

from lab import views

urlpatterns = patterns('',
    #url(r'^$', PostsListView.as_view(), name='list'), # URL http://<sitename>/blog/ 
    url(r'^$', views.index, name='index'),
    
    #url(r'^student/(?P<student_id>\d+)/$', views.student, name='student'),
    url(r'^students/(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='student'),
    url(r'^students/$', views.StudentListView.as_view(), name='students'),
    
    url(r'^professors/(?P<pk>\d+)/$', views.ProfessorDetailView.as_view(), name='professor'),
    url(r'^professors/$', views.ProfessorListView.as_view(), name='professors'),
    
    url(r'^groups/(?P<pk>\d+)/$', views.GroupDetailView.as_view(), name='group'),
    url(r'^groups/$', views.GroupListView.as_view(), name='groups'),
    
    url(r'^schedule/$', views.schedule, name='schedule'),
    
    url(r'^homework/(?P<subject_id>\d+)/$', views.homework, name='homework'),
    
    url(r'^result/(?P<lab_id>\d+)/$', views.lab_results, name='lab_results')
    #url(r'^result/stud/(?P<subject_id>\d+)/$', views.stud_results, name='stud_results')
    
    ##url(r'^professor/register/$', views.professor_register, name='register'),
    ##url(r'^professor/login/$', views.professor_login, name='login'),
    #url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://<sitename>/blog/<number>/ 
                                              

)
