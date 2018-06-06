"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from karmo.views import hi,take_input,create_contest,create_question,testcase,testcase_main,hii,match_testcase,exsisting_contest,problem,question

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', exsisting_contest,name='home'),
    url(r'^hi/', hii),
    url(r'^take_input/',take_input,name= 'take_input'),
    url(r'^create_contest/',create_contest,name= 'create_contest'),
    url(r'^create_question/',create_question,name= 'create_question'),
    url(r'^testcase/',testcase,name= 'testcase'),
    url(r'^testcase_main/',testcase_main,name= 'testcase_main'),
    url(r'^match_testcase/',match_testcase,name= 'match_testcase'),
    url(r'^contests/$',exsisting_contest,name= 'exsisting_contest'),
    url(r'^contests/(?P<pk>\d+)/$',problem,name= 'problem'),
    url(r'^problem/(?P<pk>\d+)/$',question,name= 'question'),    

]
