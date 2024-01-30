from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def home(request):
    try:
        fullname=request.session['Name']
        return render(request,'app/home.html',{'guest':fullname})
    except:
        return render(request,'app/home.html')



# def base(request):
#     return render(request,'app/base.html')

def Signup(request):
    try:
        fullname=request.session['Name']
        return render(request,'app/Signup.html',{'guest':fullname})
    except:
        return render(request,'app/Signup.html')

def Login(request):
    try:
        fullname=request.session['Name']
        return render(request,'app/Login.html',{'guest':fullname})
    except:
        return render(request,'app/Login.html')

def about(request):
    try:
        fullname=request.session['Name']
        return render(request,'app/about.html',{'guest':fullname})
    except:
        return render(request,'app/about.html')


def Contact(request):
    try:
        fullname=request.session['Name']
        return render(request,'app/Contact.html',{'guest':fullname})
    except:
        return render(request,'app/Contact.html')
      
def Services(request):
    try:
        fullname=request.session['Name']
        return render(request,'app/Services.html',{'guest':fullname})
    except:
        return render(request,'app/Services.html')

def savedata(request):
    name=request.POST['Name']
    email=request.POST['email']
    contact=request.POST['number']
    city=request.POST['city']
    password=request.POST['password']

    request.session['Name']=name
    request.session['E-mail']=email
    request.session['Contact']=contact
    request.session['City']=city
    request.session['Password']=password
    
    return render(request,'app/Login.html')

def Login_data(request):
    if request.POST:
        email=request.POST['email']
        pwd=request.POST['password']


        if 'E-mail' in request.session:
            emailid=request.session['E-mail']
            pswd=request.session['Password']
            
            if email==emailid and pwd==pswd:
                name=request.session['Name']
                request.session.modified= True 

                return render(request,'app/home.html',{'guest':name})
            else:
                ms="Incorrect password or E-mail"
                return render(request,'app/Login.html',{'incoreectmsg':ms})
        else:
            msg = "Either Session expired or sessionid not set..........."
            return render(request,'App/Signup.html',{'msg1':msg})   
    else:
        msg1 = "Session expired..........."
        return render(request,'app/Signup.html',{'msg1':msg1})


def delete(request):
    if 'Name' in request.session:
        del request.session['Name']
        request.session.flush()
   
    return render(request,'app/Signup.html')


# def logindata(request):
#     if request.POST:
#         emailid =request.POST['email']
#         password = request.POST['password']

#         # email_id = request.COOKIES['email']                               # get-cookie
#         # pwd = request.COOKIES['password']                                 # get-cookie
#         if 'email' in request.session:
#             email_id = request.session['email']                                 # get-session
#             pwd = request.session['password']                                   # get-session
#             if email_id==emailid and password==pwd:
#                 name = request.session['fname']
#                 request.session.modified = True 
#                 return render(request,'dashboard.html',{'data':name})
#             else:
#                 name="Details not matched"
#                 return render(request,'sign_in.html',{'data':name})
#         else:
#             msg = "Either Session expired or sessionid not set..........."
#             return render(request,'sign_up.html',{'msg1':msg})
#     else:   
#             msg = "Session expired..........."
#             return render(request,'sign_up.html',{'msg1':msg})




    