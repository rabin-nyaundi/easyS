from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CreateUser
from .models import Building, UserProfile

# Create your views here.


@login_required(login_url='login')
def index(request):
    buildings = Building.objects.all()
    if buildings:
        if request.method == 'GET':
            # return HttpResponse("Method not allowed")
            return render(request, 'rentals/index.html',
                {'buildings': buildings}
            )    
        
        else:
            return HttpResponse("Method not allowed")
        
    return render(request, 'rentals/index.html',
        { 'messages' : "No buildings found" }
    )
        
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('index')
        return HttpResponse("User does not exists")
        
    return render(request, 'rentals/login.html')

def register_view(request):
    if request.method == 'POST':
        user_register_form = CreateUser(request.POST)
        
        if user_register_form.is_valid():
            user = user_register_form.save()
            user.set_password(user.password)
            user.save()
            
            return redirect('login')
        
        return redirect('register')
    else:
        user_register_form=CreateUser()
    return render(request, 'rentals/register.html',
            {
                'user_register_form': user_register_form
            })

def logout_view(request):
    logout(request)
    return redirect('login')

def add_building_view(request):
    if request.method == 'POST':
        # return HttpResponse("<h1>Failed</h1>")
        # users = request.user.id
        # str(UserProfile.objects.get(id)) 
        
        name = request.POST.get('name')
        location = request.POST.get('location')
        owner = request.POST.get('owner')
        units = request.POST.get('units')
        
        building = Building(name=name, location=location,
                            owner=owner, units_count=units)
        building.save()
        
        buildings = Building.objects.all()
        
        return render(request, 'rentals/index.html',{
            'messages': 'Added successfully',
            'buildings' : buildings
        })
        
        return render(request, 'rental/index.htnl')
        
    if request.method == "GET":
        # return HttpResponse("Failed")
        return render(request, 'rentals/addBuilding.html')

def update_building_view(request, id):
    
    if request.method == 'GET':
        building=Building.objects.get(id = id)
        return render(request,'rentals/update.html',
                { 'building':building })
        
    if request.method == 'POST':
        
        name = request.POST.get('name')
        location = request.POST.get('location')
        owner = request.POST.get('owner')
        units = request.POST.get('units')
        
        buildings = Building.objects.all()
        
        Building.objects.filter(id=id).update(name=name, location=location,
                            owner=owner, units_count=units)
        # building.save()
        return render(request, 'rentals/index.html', {
            'messages': 'Updated Successfully',
            'buildings': buildings
        })
        
        
        
