from django.shortcuts import render,redirect
from .models import Building
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def index(request):
    buildings = Building.objects.all()
    context = {"buildings":buildings}
    return render(request,'realestate/index.html',context)

def about(request):
    return render(request,'realestate/about.html')    

def contact(request):
    return render(request,'realestate/contact.html')

def buildingShow(request,id):
    building = Building.objects.get(id=id)
    context = {"building":building}
    return render(request,'realestate/property-single.html',context)

@login_required(login_url="/accounts/login")
def createPost(request):
    if request.method == "POST":
        type = request.POST.get('selectbuilding')
        forwhat = request.POST.get('forwhat')
        area = request.POST.get('area')
        price = request.POST.get('price')
        address = request.POST.get('address')
        images = request.FILES.getlist('images')
        description = request.POST.get('description')
        rooms = request.POST.get('rooms')
        bathroom = request.POST.get('bathroom')
                 
        if type == "shaga":
            type="شقة"
        elif type == "mahal":
            type = "محل"
        elif type == "omara":
            type = "عمارة"
        elif type == "vela":
            type = "فيلا"
        elif type == "shaleh":
            type = "شالية"
        elif type == "studio":
            type = "استوديو"
        elif type == "duplex":
            type = "دولكس"


        if forwhat == "2":
            forwhat = "للبيع"
        else:
            forwhat = "للايجار"
        
        
        Building.objects.create(
            publisher = request.user,
            type = type,
            forwhat=forwhat, 
            area=area, 
            price=price, 
            address=address,
            images = images,
            description=description,
            rooms=rooms,
            bathroom = bathroom,

        )
            

        messages.success(request, 'Post created')
        return redirect("/")

    context = {}
    return render(request,'realestate/createpost.html',context)



def profile(request):
    buildings = Building.objects.filter(publisher=request.user)
    context = {"buildings":buildings}
    return render(request,'realestate/profile.html',context)