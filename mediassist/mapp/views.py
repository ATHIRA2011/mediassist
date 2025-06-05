from django.shortcuts import render,redirect
from . models import Meg_tbl,ME_tbl

# Create your views here.
def index(request):
    return render(request,"index.html")
def reg(request):
    if request.method=='POST':
        fname = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        pssw = request.POST.get('password')
        obj = Meg_tbl.objects.create(fnm=fname, mob=mobile, eml=email, psw=pssw)
        obj.save()
        if obj:
            return render(request,"home.html")
        else:
            return render(request,"reg.html")
    return render(request,"reg.html")


def log(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        passw = request.POST.get('password')
        obj = Meg_tbl.objects.filter(eml=email, psw=passw)
        if obj:
            request.session['ema'] = email
            request.session['psa'] = passw
            for m in obj:
                idno = m.id
                request.session['idl'] = idno
            return render(request, "home.html")
        else:
            msg = "invalid email"
            request.session['ema'] = ' '
            request.session['psa'] = ' '
            return render(request, "log.html", {"error": msg})
    
    return render(request, "log.html")

def user(request):
    obj= Meg_tbl.objects.all()

    return render(request,"user.html",{"data":obj})


def edit(request,idl):
    obj=Meg_tbl.objects.filter(id=idl)
    if request.method=='POST':
        fnm=request.POST.get('fn')
        idl=request.POST.get('idno')
        mob=request.POST.get('mob')
        eml=request.POST.get('eml')
        psw=request.POST.get('psw')
        obc= Meg_tbl.objects.filter(id=idl)
        obc.update(fnm=fnm, mob=mob, eml=eml, psw=psw)
        return redirect("/user")
    return render(request,"edit.html",{"data":obj}) 
def delete(request,idl):
    obj=Meg_tbl.objects.filter(id=idl)
    obj.delete()
    return redirect("/user")

def medicine(request):
    if request.method=='POST':
        mname = request.POST.get('mn')
        price = request.POST.get('pr')
        imag = request.FILES.get('im')
        desc = request.POST.get('ds')
        obj = ME_tbl.objects.create(mnm=mname,prc=price,im=imag,des=desc)
        obj.save()
        if obj:
            return render(request,"medicine.html",{"msg":"details uploades.."})

        
    return render(request,"medicine.html")
   
def medicineview(request):
    obj = ME_tbl.objects.all()
    return render(request,"medicineview.html",{"medicine":obj})

