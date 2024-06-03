"""
URL configuration for SkinCareRoutine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from SkinCareApp.views import HomePageView, SkinTypeFormView, RoutineProductsView, AddUserView, LoginView, AboutSkinTypesView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name="index"),
    path('home/', HomePageView.as_view(), name="index"),
    path("skin-type-form/", (SkinTypeFormView.as_view()), name="skin_type_form"),
    path('skin-type-result/', SkinTypeFormView.as_view(), name='skin_type_result'),
    path('routine-products/<str:skin_type>/', RoutineProductsView.as_view(), name='routine_products'),
    path("login/", LoginView.as_view(), name="login_view"),
    path("add-user/", AddUserView.as_view(), name="add_user"),
    path("about-skin-types/", AboutSkinTypesView.as_view(), name="about_skin_types"),
]
