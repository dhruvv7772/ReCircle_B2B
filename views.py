from django.http import HttpResponse
from django.shortcuts import render

def CollectionDash(request):
    return render(request, 'CollectionDash.html')

def DispatchForm1(request):
    return render(request, 'DispatchForm1.html')

def CollectionDashDetails(request):
    return render(request, 'CollectionDashDetails.html')

def DispatchForm2(request):
    return render(request, 'DispatchForm2.html')

def DispatchForm3(request):
    return render(request, 'DispatchForm3.html')

def HomePage(request):
    return render(request, 'HomePage.html')

def InwardChoices(request):
    return render(request, 'InwardChoices.html')

def InwardForm1(request):
    return render(request, 'InwardForm1.html')

def InwardForm2(request):
    return render(request, 'InwardForm2.html')

def Login(request):
    return render(request, 'Login.html')

def Outwardchoices(request):
    return render(request, 'Outwardchoices.html')

def RegisterVendorPage2(request):
    return render(request, 'RegisterVendorPage2.html')

def RegisterVendorSuccess(request):
    return render(request, 'RegisterVendorSuccess.html')

def RegistorVendorForm1(request):
    return render(request, 'RegistorVendorForm1.html')

def SignUp(request):
    return render(request, 'SignUp.html')

def SuccessDispatch(request):
    return render(request, 'SuccessDispatch.html')

def SuccessInward(request):
    return render(request, 'SuccessInward.html')

def SuccessOutward(request):
    return render(request, 'SuccessOutward.html')

def Admin_Dashboard(request):
    return render(request, 'index.html')

def SavedDrafts(request):
    return render(request, 'SavedDrafts.html')

def ProfilePage(request):
    return render(request, 'ProfilePage.html')


