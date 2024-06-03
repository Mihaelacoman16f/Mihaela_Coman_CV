from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import SkinTypeForm
from SkinCareApp.models import SkinType, SkincareProduct, SkincareRoutine, RoutineSkinType, AboutSkinTypes
from django.contrib.auth.models import User
from .forms import LoginForm, AddUserForm
from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
import re



class HomePageView(View):
    def get(self, request):
        return render(request, "index.html")



class SkinTypeFormView(View):
    # @login_required(login_url='/login/')
    def get(self, request):
        form = SkinTypeForm()
        return render(request, "skincare_form.html", {"form": form})
    
    def post(self, request):
        dry_skin =request.POST.get('dry_skin')
        oily_t_zone = request.POST.get('oily_t_zone')
        large_pores = request.POST.get('large_pores')
        cold_feel = request.POST.get('cold_feel')
        cream_absorption = request.POST.get('cream_absorption')
        acne_prone = request.POST.get('acne_prone')
        irritated_skin = request.POST.get('irritated_skin')

        if dry_skin == "Yes" and oily_t_zone == 'No' and large_pores == 'No' and cold_feel== "Tight" and cream_absorption == "Fast" and acne_prone == "No acne" and irritated_skin == "No":
            skin_type_name = 'Dry Skin'
        elif not dry_skin == 'No' and oily_t_zone == 'Yes' and large_pores == 'Yes' and cold_feel== "Normal" and cream_absorption == "Slow" and acne_prone == "Few acne, maximum 5" and irritated_skin == "No":
            skin_type_name = 'Oily Skin'
        elif dry_skin == 'No' and oily_t_zone == 'No' and large_pores == 'No' and cold_feel== "Normal" and cream_absorption == "Fast" and acne_prone == "No acne" and irritated_skin == "No":
            skin_type_name = 'Normal Skin'
        elif dry_skin == 'Yes' and oily_t_zone == 'No' and large_pores == 'No' and cold_feel== "Tight" and cream_absorption == "Fast" and acne_prone == "Many acne, more than 10" and irritated_skin == "Yes":
            skin_type_name = 'Sensitive Skin'
        else:
            skin_type_name = 'Combination Skin'

        skin_type = SkinType.objects.get(name=skin_type_name)

        return render(request, 'skin_type_result.html', {'skin_type': skin_type})
    

    
class RoutineProductsView(View):
    def get(self, request, skin_type):
        skin_type_result = SkinType.objects.get(name=skin_type)
        routines = SkincareRoutine.objects.filter(skin_types=skin_type_result)
        return render(request, 'routine_products.html', {'skin_type': skin_type_result, 'routines': routines} )

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login_view.html", {"form": form})


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, "user.html")
            else:
                return HttpResponse("Authentication error!")
            
        return HttpResponse("Form error!")
    

            

class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, "add_user.html", {"form": form })
    
    def post(self, request):
        form = AddUserForm(request.POST)
       
        if form.is_valid():
            username = form.cleaned_data["username"]
            password_1 = form.cleaned_data["password_1"]
            password_2 = form.cleaned_data["password_2"]
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            email = form.cleaned_data["email"]
            if len(User.objects.filter(username=username)) > 0:
                return HttpResponse("User already exists!")
            if password_1 != password_2:
                return HttpResponse("Passwords do not match!")
            
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

            if not re.fullmatch(regex, email):
                return HttpResponse("Email is not valid!")
            User.objects.create_user(username=username, password=password_1, first_name=name, last_name=surname, email=email)
            request.session["message"] = "User was created!"
            return redirect("login_view")
        return HttpResponse("Form is not valid!")
    

class AboutSkinTypesView(View):
    def get(self, request):
        skin_types = AboutSkinTypes.objects.all()
        return render(request, 'about_skin_types.html', {'skin_types': skin_types})