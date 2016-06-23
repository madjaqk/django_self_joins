from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	context = {
		"users": User.manager.all()
	}
	return render(request, "friends/index.html", context)

def create(request):
	if request.method == "POST": 
		User.manager.create_new_user(request.POST['name'])

	return redirect("/friends")

def show(request, id):
	user = User.manager.filter(id=id)

	if not user: 
		return redirect("/friends")
	else:
		context = {"user": user[0], "all_users": User.manager.exclude(id=id)}
		return render(request, "friends/show.html", context)

def update(request):
	if request.method != "POST": return redirect("/friends")

	User.manager.add_friend(request.POST["user"], request.POST["other"])

	return redirect("/friends/"+request.POST["user"])



