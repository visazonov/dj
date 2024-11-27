"""django_netology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from main.views import sample_controller, product_list, product_details
from demo.views import hello, sum, pagi

from django.conf import settings
from django.conf.urls.static import static

from orm.views import create_car, list_car, create_person
from orm.views import create_car, list_car, create_person, list_person


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", sample_controller, name="index"),
    path("products/", product_list, name="list"),
    path("products/<int:product_id>/", product_details, name="details"),
    path("hello/", hello),
    path('sum/<int:op1>/<int:op2>/', sum),
    path('pagi/', pagi),
    # path('admin/', admin.site.urls),
    path('new_car/', create_car),
    path('cars/', list_car),
    path('new_person/', create_person),
    path('people/', list_person),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
