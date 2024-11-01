from lib2to3.fixes.fix_input import context

from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

from shop.models import Category,Product

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def allcategories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'category.html',context)

def allproducts(request,p):
    c=Category.objects.get(id=p)
    p=Product.objects.filter(category=c)
    context={'cat':c,'product':p}
    return render(request,'products.html',context)



def productdetails(request,p):
    pro=Product.objects.get(id=p)
    context={'product':pro}
    return render(request,'details.html',context)




def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()
        else:
            return HttpResponse("Password are not same")
        return redirect('shop:category')
    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:category')
        else:
            messages.error(request,"invalid credentials")

    return render(request,'login.html')
# @login_required()
def user_logout(request):
    logout(request)
    return redirect('shop:category')



def addcategory(request):
    if(request.method == "POST"):
        n=request.POST['n']
        img=request.FILES['img']
        d=request.POST['d']
        c=Category.objects.create(name=n,image=img,desc=d)
        c.save()
        return redirect('shop:category')

    return render(request,'addcategory.html')

def addproduct(request):
    if(request.method == "POST"):
        n=request.POST['n']
        img=request.FILES['img']
        d=request.POST['d']
        s=request.POST['s']
        p=request.POST['p']
        c=request.POST['c']
        cat=Category.objects.get(name=c)  #category object/record matching with c
        p=Product.objects.create(name=n,image=img,desc=d,stock=s,price=p,category=cat)     #assign each value to product fields
        p.save()
        return redirect('shop:category')
    return render(request,'addproduct.html')






def addstock(request,p):
    product=Product.objects.get(id=p)
    if(request.method=="POST"):
        product.stock=request.POST['n']
        product.save()
        return redirect('shop:category')
    context={'pro':product}
    return render(request,'addstock.html',context)

