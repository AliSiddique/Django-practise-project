"""mysite URL Configuration

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
from newone.views import Dashboard, LeadDetail, LeadList, LeadCreate, Signup, Login,LogOut, LeadUpdate
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LeadList.as_view(), name="list"),
    path("<int:pk>/detail", LeadDetail.as_view(), name="detail"),
    path("create/", LeadCreate.as_view(), name="create"),
    path("<int:pk>/update", LeadUpdate.as_view(), name="update"),
    path("dashboard", Dashboard.as_view(), name="dashboard"),

   path("signup/", Signup.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
   path("logout/", LogOut.as_view(), name="logout")





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
