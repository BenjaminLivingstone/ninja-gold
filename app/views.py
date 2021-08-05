from django.shortcuts import render, redirect
from random import *
from datetime import datetime



def ninja(request):
    # context ={
    #     # "name": "farm",
    #     "gold": 0,
    #     "output":[]
    # }
    return render(request,'index.html')

def money(request, name):
    if 'gold' in request.session:
        # request.session['gold']=request.session['gold']+5
        if name=='farm':
            random=randrange(10,20)
            request.session['gold']=request.session['gold']+random
            request.session['output'].append({'text': f"Earned {random} gold from the farm, {datetime.now()} ",'color': "text-primary"})
        if name=='cave':
            random=randrange(5,10)           
            request.session['gold']=request.session['gold']+random
            request.session['output'].append({'text': f"Earned {random} gold from the cave, {datetime.now()} ",'color': "text-primary"})
        if name=='house':
            random=randrange(2,5)
            request.session['gold']=request.session['gold']+random
            request.session['output'].append({'text': f"Earned {random} gold from the farm, {datetime.now()} ",'color': "text-primary"})        
        if name=='casino':
            random=randrange(-50,50)
            request.session['gold']=request.session['gold']+random
            if random > 0: 
                request.session['output'].append({'text': f"Earned {random} gold from the casino, {datetime.now()} ",'color': "text-primary"})
                request.session.save()
            else: 
                request.session['output'].append({'text': f"Entered a casino and lost {random} gold... Ouch.., {datetime.now()}",'color': "text-danger"})
                request.session.save()              
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
        request.session['output']=[]
    return redirect("/")

def reset(request):
    request.session['gold']=0
    request.session['output']=[]
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
