from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CreateUser
from .models import Building, UserProfile, Tenant, BuildingTenant

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
        
        if request.method == 'POST':
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
        
def add_tenant_view(request):
    tenants = Tenant.objects.all()

    if request.method == "GET":
        if tenants:
            return render(request, 'rentals/addTenant.html',
                { 'tenants': tenants })
            
        return render(request, 'rentals/addTenant.html',
                             {'messages': "No tenants found"}
                             )
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        next_of_kin = request.POST.get('kin')
        
        tenant = Tenant(name=name, email=email, phone=phone,
                        next_of_kin=next_of_kin)
        tenant.save();
        return render(request, 'rentals/index.html', { 'messages' : 'Record updated successfully' })
        return HttpResponse("Failed to add tenant")
    
    
def tenants_view(request):
    tenants = Tenant.objects.all()
    if tenants:
        if request.method == 'GET':
            # return HttpResponse("Method not allowed")
            return render(request, 'rentals/tenants.html',
                          {'tenants': tenants}
                          )

        if request.method == 'POST':
            return HttpResponse("Method not allowed")

    return render(request, 'rentals/tenats.html',
                  {'messages': "No tenants found"}
                  )
    
    
def update_tenant_view(request, id):

    if request.method == 'GET':
        tenants = Tenant.objects.get(id=id)
        return render(request, 'rentals/updateTenant.html',
                      {'tenants': tenants})

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        next_of_kin = request.POST.get('kin')

        tenants = Tenant.objects.all()

        Tenant.objects.filter(id=id).update(name = name, email = email, phone = phone,next_of_kin = next_of_kin)
        # building.save()
        return render(request, 'rentals/tenants.html', {
            'messages': 'Updated Successfully',
            'tenants': tenants
        })


def buildnig_tenants_view(request):
    building_tenants = BuildingTenant.objects.all()
    if building_tenants:
        if request.method == 'GET':
            # return HttpResponse("Method not allowed")
            return render(request, 'rentals/buildingTenant.html',
                          {'building_tenants': building_tenants}
                          )

        if request.method == 'POST':
            return HttpResponse("Method not allowed")

    return render(request, 'rentals/index.html',
                  {'messages': "No building_tenants found"}
                  )
    
    
def add_b_tenant(request):
    buildings = Building.objects.all();
    tenants = Tenant.objects.all()
    b_tenant = BuildingTenant.objects.all()
    
    if request.method == "GET":
        return render(request, 'rentals/addbTenant.html',{
            'buildings': buildings,
            'tenants': tenants
        })
        
    if request.method == "POST":
        build = request.POST.get('building')
        building = Building.objects.get(id=build)
        ten = request.POST.get('tenant')
        tenant = Tenant.objects.get(id=ten)
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        status = request.POST.get('status')
        
        building_tenant = BuildingTenant(building=building, tenant=tenant, check_in_date=date,
                                         contract_amount=amount,status=status)
        building_tenant.save()
        
        return redirect('btenants')

def update_b_tenant(request, id):
    buildings = Building.objects.all()
    tenants = Tenant.objects.all()
    
    b_tenant = BuildingTenant.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'rentals/update_b_tenant.html',
                      {'b_tenant': b_tenant,
                       'buildings': buildings,
                       'tenants': tenants
                       })
        
    if request.method == 'POST':
        build = request.POST.get('building')
        building = Building.objects.get(id=build)
        ten = request.POST.get('tenant')
        tenant = Tenant.objects.get(id=ten)
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        status = request.POST.get('status')
        
        BuildingTenant.objects.filter(id=id).update(building=building, tenant=tenant, check_in_date=date,
                                                    contract_amount=amount, status=status)
        return redirect('btenants')
