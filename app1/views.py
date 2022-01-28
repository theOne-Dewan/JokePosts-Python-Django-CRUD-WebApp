from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Quote
import bcrypt

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register_user(request): 
    errors = User.objects.validate_reg(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],password=hash)
        request.session['logged_in'] = user.id
        return redirect("/quotes")


def login_user(request):
    errors = User.objects.validate_login(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['logged_in'] = user.id
        return redirect("/quotes")


def quotes(request):
    this_user = User.objects.get(id =request.session['logged_in'])
    users = User.objects.all()
    quotes = Quote.objects.all()
    context ={
        'all_users' : users,
        'current_user' : this_user,
        'all_quotes' : quotes,
    }
    return render(request, "quotes.html", context)

def logout(request, id):
    del request.session['logged_in']
    return redirect('/')

def edit(request, id):
    edit_user = User.objects.get(id = id)
    context = {
        'edit_id' : edit_user
    }
    return render(request, 'edit.html', context)

def update(request):
    errors = User.objects.validate_update(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit/'+ request.POST['update_id'])
    else:
        update_user = User.objects.get(id = request.POST['update_id'])
        update_user.first_name = request.POST['first_name']
        update_user.last_name = request.POST['last_name']
        update_user.email = request.POST['email']
        update_user.save()
        return redirect('/quotes')

def add_quote(request):
    retained_id = request.POST['quote_id']
    print('*'*50)
    print(retained_id)
    errors = User.objects.validate_quote(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quotes')
    else:
        active_user = User.objects.get(id = retained_id)
        print('*'*50)
        print(retained_id)
        new_quote = Quote.objects.create(author_name=request.POST['author'], quote = request.POST['quotes'], user= active_user)
        return redirect('/quotes')

def delete_quote(request, id):
    delete_id = id
    to_delete = Quote.objects.get(id = delete_id)
    to_delete.delete()
    return redirect('/quotes')

def user(request, id, idd):
    user_id = id
    logged_user = idd
    this_user = User.objects.get(id = user_id)
    context = {
        'user' : this_user,
        'log_id' : logged_user
    }
    return render(request, 'user.html', context)

def likes(request, id):
    like = Quote.objects.get(id = id)
    current_likes = like.likes
    new_likes = current_likes + 1
    like.likes = new_likes
    like.save()
    return redirect('/quotes')
