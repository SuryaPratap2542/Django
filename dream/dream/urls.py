"""dream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from dream import views


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.homePage,name='Home'),
    path('about/',views.about,name='About'),
    path('blog/',views.blog,name='Blog'),
    path('cart/',views.cart,name='Cart'),
    path('contact/',views.contact,name='Contact'),
    path('shop/',views.shop,name='shop'),
    path('sproduct/',views.sproduct,name='Sproduct'),
    path('userform/',views.userform,name='Userform'),

    # path('ind0/',views.ind0),
    # path('ind1/',views.ind1),
    # path('ind2/',views.ind2),
    # there are three types int , str , slug
    # path('ind2/<slug:courseid>',views.courseDetails),
]
