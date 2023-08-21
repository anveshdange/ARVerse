from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import AIverse
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'event/index.html')

def reg(request):
    return render(request, 'event/reg.html')

def admin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('username')
        loginpassword = request.POST.get('password')
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            return render(request, 'event/master.html')

    return render(request, 'event/admin_login.html')

def handlelogout(request):
    logout(request)
    return redirect("index")
def prepare_payment(request):
    name = request.POST.get('name')
    number = request.POST.get('contact')
    email = request.POST.get('email')
    branch = request.POST.get('Branch')
    year = request.POST.get('Year')
    event = request.POST.get('event')
    team_size = request.POST.get('team')
    member1 = request.POST.get('1')
    member2 = request.POST.get('2')
    member3 = request.POST.get('3')
    member4 = request.POST.get('4')
    team_members = [member1, member2, member3, member4]
    payment_data = {'name': name, 'number': number, 'email': email, 'branch': branch, 'year': year, 'event': event,'team_size': team_size, 'team_members':team_members}
    return render(request, 'event/payment.html', payment_data)
def payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('contact')
        email = request.POST.get('email')
        branch = request.POST.get('Branch')
        year = request.POST.get('Year')
        event = request.POST.get('event')
        team_size = request.POST.get('team_size')
        team_members = request.POST.get('team_member')
        screenshot = request.files["screenshot"]
        AIverse_item = AIverse(Name=name, Event=event, Branch=branch, Year=year, Email=email, Contact=number, Team_Size=team_size, team_member=team_members, transaction=screenshot)
        AIverse_item.save()
        return redirect("index")

