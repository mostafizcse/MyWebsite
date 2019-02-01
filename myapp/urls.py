"""personalblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from myapp.views import email
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.getLogin, name="login"),
    path('logout', views.getlogout, name="logout"),
    path('emerging_tecnologies/', views.emerging_tecnologies, name="emerging_tecnologies"),
    path('event',views.get_event,name="event"),
    path('post_details/<int:post_id>', views.post_details, name="post"),
    path('create', views.getcreate, name="create"),
    path('careers', views.getcarear, name="careers"),
    path('abc/<int:cariar_id>',views.cariar_details,name="cariardetails"),
    path('index2', views.add_menu, name="index2"),
    path('mdetails/<int:menu_id>',views.menu_details, name="mdetails"),
    path('menucreate', views.getmenucreate, name="menucreate"),
    path('register', views.getRegister, name="register"),
    path('basehtml', views.getbasehtml, name="basehtml"),
    path('deshbord', views.getadmin, name="templat"),
    path('requermentCreate',views.requirments_Create, name="requermentCreate"),
    path('sliderCreate',views.slider_Create, name="sliderCreate"),
    path('reviewlistCreate',views.reviewlist_Create, name="reviewlistCreate"),
    path('teamCreate',views.team_create, name="teamCreate"),
    path('eventCreate',views.event_Create, name="eventCreate"),
    path('featurlistCreate',views.featurlist_Create, name="featurlistCreate"),
    path('update/<int:pid>',views.getUpdate, name="update"),
    path('delete/<int:pid>',views.getDelete, name="delete"),
    path('sliderupdate/<int:pid>',views.getsliderUpdate, name="sliderupdate"),
    path('sliderdelete/<int:pid>',views.getsliderDelete, name="sliderdelete"),
    path('createupdate/<int:pid>',views.getcreateUpdate, name="createupdate"),
    path('createdelete/<int:pid>', views.getcreateDelete, name="createdelete"),
    path('manuupdate/<int:pid>',views.getmanuUpdate, name="manuupdate"),
    path('manudelete/<int:pid>', views.getmanuDelete, name="manudelete"),
    path('requermerntUpdate/<int:pid>',views.getRequermerntUpdate, name="requermerntUpdate"),
    path('requermerntdelete/<int:pid>', views.getrequermerntDelete, name="requermerntdelete"),
    path('reviewlistUpdate/<int:pid>',views.getreviewlistUpdate, name="reviewlistUpdate"),
    path('reviewlistdelete/<int:pid>', views.getreviewlistDelete, name="reviewlistdelete"),
    path('teamlistUpdate/<int:pid>',views.getteamlistUpdate, name="teamlistUpdate"),
    path('teamlistdelete/<int:pid>', views.getteamlistDelete, name="teamlistdelete"),
    path('feuterslistUpdate/<int:pid>',views.getfeuterslistUpdate, name="feuterslistUpdate"),
    path('feuterslistdelete/<int:pid>', views.getfeuterslistDelete, name="feuterslistdelete"),
    path('email', email.as_view()),
    path('contact', views.contact_view, name="contact"),

]
