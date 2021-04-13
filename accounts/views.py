from django.shortcuts import render, redirect
from .models import profile
from .forms import SignupForm ,UserForm ,ProfileForm
from django.contrib.auth import authenticate,login

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username ,password=password)
            login(request,user)
            return redirect('/accounts/profile')
             
    else:
        form = SignupForm ()
    
    return render(request,'registration/signup.html',{
        'form':form    
    })
    
def myprofile(request):
    profiles = profile.objects.get(user=request.user)
    return render(request ,'profile/myprofile.html',{'profiles':profiles})
    
    
def myprofile_edit(request):
    myprofile=profile.objects.get(user=request.user)
    if request.method=='POST':
        userform = UserForm(request.POST ,instance=request.user)
        profileform = ProfileForm(request.POST, instance=myprofile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            m_profile=profileform.save(commit=False)
            m_profile.user=request.user
            m_profile.save()
            return redirect('/accounts/profile')
            
    else:  #show
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=myprofile)
        
    return render(request ,'profile/myprofile_edit.html',{
        'userform':userform,
        'profileform':profileform
    })

