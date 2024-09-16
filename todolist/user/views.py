from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def userprofile(request):
    user = User.objects.all()
    return render(request,'user/defaultuserprofile.html',{'user':user})