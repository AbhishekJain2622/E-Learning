from django.shortcuts import render,redirect
from django.contrib import messages
from internal.models import Contact,Blogs,Internship,ProgrammingLanguage,Post,Service
# Create your views here.
def home(request):
    work=Post.objects.all()
    service=Service.objects.all()
    context={"works":work,'services':service}
    return render(request,'home.html',context)
    


def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,'handleblog.html',context)

def langauges(request):
    posts=ProgrammingLanguage.objects.all()
    context={"posts":posts}
    return render(request,'home.html',context)
    


def about(request):
    return render(request,'about.html')

def success(request):
    return render(request,'success.html')


def cart(request):
    return render(request,'cart.html')

"""def courses(request):
    cname=Course.objects.all()
    context={"cnames":cname}
    return render(request,'course.html',context)"""
    
def internshipdetails(request):

    if not request.user.is_authenticated:
        messages.warning(request,"Please login to access this page")
        return redirect("/auth/login/")

    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fusn=request.POST.get('usn')
        fcollege=request.POST.get('cname')
        fcourse=request.POST.get('course')
        fprogramming_langauge=request.POST.get('programming_langauge')
        """fstartdate=request.POST.get('startdate')
        fenddate=request.POST.get('enddate')"""


# converting to upper case
        fname=fname.upper()
        fusn=fusn.upper()
        fcollege=fcollege.upper()
        fprogramming_langauge=fprogramming_langauge.upper()
        fcourse=fcourse.upper()
        

        # 
        check1=Internship.objects.filter(usn=fusn)
        check2=Internship.objects.filter(email=femail)

        if check1 or check2:
            messages.warning(request,"Your Details are Stored Already")
            return redirect("/internshipdetails")

        query=Internship(fullname=fname,usn=fusn,email=femail,college_name=fcollege,course=fcourse,programming_langauge=fprogramming_langauge)
        query.save()

        messages.success(request,"Form is Submitted Successful!")
        return redirect('/internshipdetails')

    return render(request,'intern.html')


def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you Soon!")

        return redirect('/contact')

    return render(request,'contact.html')
        

