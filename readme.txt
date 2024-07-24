django-admin startproject registration .
python3 manage.py startapp app1
installed apps app1, templates
create templates folder
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Create an Account</h2>
        <form action="/register/" method="POST">
            {% csrf_token %}
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <label for="confirm_password">Confirm Password:</label>
                <input type="password" id="confirm_password" name="confirm_password" required>
            </div>
            <button type="submit">Sign Up</button>
        </form>
        <p>Already have an account? <a href="/login/">Log in here</a></p>
    </div>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <form action="/login/" method="POST">
            {% csrf_token %}
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
        </form>
        <p>Don't have an account? <a href="/signup/">Sign up here</a></p>
    </div>
</body>
</html>
create static/style
.container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
    box-sizing: border-box;
    margin-top: 5px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 3px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

p {
    margin-top: 10px;
}

a {
    color: #007bff;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    'registration/static'
]

views.py
from django.shortcuts import render

# Create your views here.

def HomePage(request):
    pass


def SignupPage(request):
    pass


def LoginPage(request):
    pass
path('', views.SignupPage, name='signup'),

def SignupPage(request):
    return render(request,'signup.html')

path('login/', views.LoginPage, name='login'),

def LoginPage(request):
    return render(request,'login.html')


path('home/', views.HomePage, name='home'),

def HomePage(request):
    return render(request,'home.html')
template home.html
bootstrap starter template

python migrate 
python3 manage.py createsuperuser

login admin panel
lola, lola,a@a.com

we have to get dTA frm signup form so
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')#from input field name
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        print(uname,email,password1,password2)
    return render(request,'signup.html')

mnm mnm@m.com poiuy09 poiuy09 printed when refresh
network submit payload
csrf omit forbidden error

from django.contrib.auth.models import User
usermodel import from django

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')#from input field name
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        
        my_user = User.objects.create_user(uname,email, password1)
        my_user.save()
        return HttpResponse("user has been created successfully")
        print(uname,email,password1,password2)
    return render(request,'signup.html')


    create a new user at signup page then check in admin panel,users 
create another b4 do above steps
            my_user = User.objects.create_user(uname,email, password1)
        my_user.save()
        # return HttpResponse("user has been created successfully")
        return redirect('login')
        # print(uname,email,password1,password2)
    return render(request,'signup.html')
    another created
    mistake confirm correct form constraint apply


            if(password1!=password2):
            return HttpResponse("ur password was not entered correctly")
        else:
            my_user = User.objects.create_user(uname,email, password1)
            my_user.save()
        # return HttpResponse("user has been created successfully")
            return redirect('login')

now loginpage
def LoginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')#from input field name
        password = request.POST.get('password')#from input field name
        print(uname,password)
    return render(request,'login.html')

    give wrong print

    from django.contrib.auth import authenticate,login

    def LoginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')#from input field name
        password = request.POST.get('password')#from input field name
        print(uname,password)
        user = authenticate(request,username=uname,password=password)#
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password incorrect!!!")
            
    return render(request,'login.html')

    authenticate matches login ones and signup ones

      <a href="{%url 'logout'%}" class="btn btn-primary">logout</a>
      in home logout button


          path('logout/', views.LogOut, name='logout'),
def LogOut(request):
    logout(request)
    return redirect('login')

    from django.contrib.auth import authenticate,login,logout


    check if works

    bug here
    we search home it comes

decorater if authentication then home

from django.contrib.auth.decorators import login_required
@login_required(login_url='login') 
if not correct it stays at login

already have an account correct