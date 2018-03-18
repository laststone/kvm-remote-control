from django.conf.urls import url
from . import views

urlpatterns=[
 	url(r'^$',views.index),
 	url(r'^(\d+)$',views.show),
 	url(r'^vmx$',views.vmx),
 	url(r'^vmx_start_(\w+)$',views.start),
 	url(r'^vmx_shut_(\w+)$',views.stop),
 	url(r'^vmx_suspend_(\w+)$',views.suspend),
 	url(r'^vmx_resume_(\w+)$',views.resume)

 ]
