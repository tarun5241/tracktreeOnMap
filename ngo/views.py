from django.shortcuts import render, redirect
from django.contrib import messages
from ngo.models import Ngo, Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.models import User

# import folium library
import folium

# create a map object

@login_required(login_url='login')
def map(request,pk):

    ngo = Ngo.objects.get(id=pk)
    print("ngo stance ",ngo)
    
    events = Event.objects.filter(ngo_name=ngo.id)
    # print("Event",event)
    # context = { 'ngo' : ngo , 'events' : events}
    
    mapObj = folium.Map(location=[24.2170111233401, 81.0791015625000],
                    zoom_start=5)

#   # add a marker object to the map
    for event in events:
        folium.Marker(location=[event.latitude, event.longitude],
              icon=folium.Icon(icon='tree', prefix='fa', color='green'),
              popup=folium.Popup(
                  f"<p>Event Date  : <b>{event.event_date}</b></p><p>Name of Tree Saplings Planted :<b> {event.tree_name}</b></p><p>Total Saplings Planted : <b>{event.trees_planted}</b>", max_width=500),
              tooltip=f'<b>{event.event_name}</b>'
              ).add_to(mapObj)
    
    
    m = mapObj._repr_html_()
    context = {
        'm': m,

    }


    return render(request, 'ngo/map.html', context)

# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            print("User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            # user = Ngo.objects.get(name=username)
            # return ngoProfile(request,user.id)
            return redirect('index')
            # return render(request, 'ngo/profile.html',user)
    return render(request, 'ngo/login.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return render(request,'ngo/login.html')


def index(request):
    ngos = Ngo.objects.all()
    context = { 'ngos' : ngos }
    return render(request, 'ngo/index.html',context)

@login_required(login_url='login')
def ngoProfile(request,pk):
    # user = User.objects.get(id=pk)
    ngo = Ngo.objects.get(id=pk)
    event = Event.objects.filter(ngo_name=ngo.id)
    
    context = { 'ngo' : ngo , 'events' : event}

    return render(request, "ngo/profile.html", context)




def login1(request):
    return render(request, 'ngo/login.html')



def signup(request):
    return render(request, 'ngo/createUser.html')


@login_required(login_url='login')
def createEvent(request,pk):
    ngo = Ngo.objects.get(id=pk)
    context = {'user': ngo}
    return render(request, 'ngo/addEvent.html',context)

def register(request,pk):
    ngo = Ngo.objects.get(id=pk)
    context = {'user': ngo}
    return render(request, "ngo/register.html", context)



def createUser(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['password']

        # Create the user
        myuser = User.objects.create_user(username, email, pwd)
 
        myuser.save()
        context = {'user' : username}
        messages.success(request, " Your Account has been successfully created")
        return redirect('login')

    else:
        return redirect('signup')


@login_required(login_url='login')
def createNgo(request,pk):
    ngo = Ngo.objects.get(id=pk)
    if request.method == 'POST':
        ngo.ngo_name = request.POST.get('ngo_name')
        ngo.email= request.POST.get('email')
        ngo.mission = request.POST.get('mission')
        ngo.address = request.POST.get('address')
        ngo.total_member = request.POST.get('total_member')

        ngo.save()
        user = Ngo.objects.get(id=pk)
        context = { 'ngo' : user }
        messages.success(request,"Upadate Successfully")
        return render(request, "ngo/profile.html", context)


    context = {'form': ngo}
    return render(request, "ngo/profile.html", context)



@login_required(login_url='login')
def event(request,pk):
    # user = User.objects.get(id=pk)
    ngo = Ngo.objects.get(id=pk)
    event = Event.objects.filter(ngo_name=ngo.id)
    context = { 'ngo' : ngo , 'events' : event}
    return render(request, "ngo/events.html", context)

@login_required(login_url='login')
def addEvent(request,pk):
    ngo = Ngo.objects.get(id=pk)
    if request.method=="POST":
        # Get the post parameters
        # ngo_name=request.POST.get('ngo_name')
        event_name=request.POST.get('event_name')
        event_date=request.POST.get('event_date')
        tree_name = request.POST.get('tree_name')
        trees_planted = request.POST.get('trees_planted')
        latitude=request.POST.get('latitude')
        longitude=request.POST.get('longitude')

        event = Event(ngo_name=Ngo.objects.get(id=pk), event_name=event_name, 
                        event_date=event_date, tree_name=tree_name, 
                        trees_planted=trees_planted, latitude=latitude, longitude=longitude )
        event.save()
        
        event = Event.objects.filter(ngo_name=ngo.id)
    
        ngo = Ngo.objects.get(id=pk)
        context = { 'ngo' : ngo , 'events' : event}

        return render(request, "ngo/profile.html", context)

    else:
        return redirect('signup')

