from django.shortcuts import render, redirect
from random import *

def ninja(request):
    context ={
        "name": "farm",
        "gold": 0,
    }
    return render(request,'index.html', context)

def money(request, name):
    if 'gold' in request.session:
        # request.session['gold']=request.session['gold']+5
        if name=='farm':
            request.session['gold']=request.session['gold']+randrange(10,20)
        if name=='cave':
            request.session['gold']=request.session['gold']+10
        if name=='house':
            request.session['gold']=request.session['gold']+20
        if name=='casino':
            request.session['gold']=request.session['gold']+100                               
        # if request.POST['game']=='farm':
        #     pass
        # if request.POST['gold']=='cave':
        #     pass
        # if request.POST['gold']=='house':
        #     pass
        # if request.POST['gold']=='casino':
        #     pass
    else:
        request.session['gold']=0
    return redirect("/")

def reset(request):
    request.session['gold']=0
    return redirect("/")

# import random
# def randInt(min=0,max=100):
#     num = (random.random() * (max-min)+min)
#     return round(num)
# print(randInt(10,20))

# def random_word(request):
#     if 'count' in request.session:
#         request.session['count']=request.session['count']+1
#     else:
#         request.session['count']=1
#     context = {
#         "title": "Random Word",
#         "word": get_random_string(length=14),
#     }
#     return render(request,'app/index.html', context)

# def reset(request):
#     request.session['count']=0
#     return redirect("/")
