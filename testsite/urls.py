from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("/", views.index, name='', name='index'),
    path('CollectionDash/', views.CollectionDash, name='CollectionDash'),

    path('DispatchForm1/', views.DispatchForm1, name='DispatchForm1'),

    path('CollectionDashDetails/', views.CollectionDashDetails, name='CollectionDashDetails'),

    path('DispatchForm2/', views.DispatchForm2, name='DispatchForm2'),

    path('DispatchForm3/', views.DispatchForm3, name='DispatchForm3'),

    path('HomePage/', views.HomePage, name='HomePage'),

    path('InwardChoices/', views.InwardChoices, name='InwardChoices'),

    path('InwardForm1/', views.InwardForm1, name='InwardForm1'),

    path('InwardForm2/', views.InwardForm2, name='InwardForm2'),

    path('', views.Login, name='Login'),

    path('Outwardchoices/', views.Outwardchoices, name='Outwardchoices'),

    path('RegisterVendorPage2/', views.RegisterVendorPage2, name='RegisterVendorPage2'),

    path('RegisterVendorSuccess/', views.RegisterVendorSuccess, name='RegisterVendorSuccess'),

    path('RegistorVendorForm1/', views.RegistorVendorForm1, name='RegistorVendorForm1'),

    path('SignUp/', views.SignUp, name='SignUp'),

    path('SuccessDispatch/', views.SuccessDispatch, name='SuccessDispatch'),

    path('SuccessInward/', views.SuccessInward, name='SuccessInward'),

    path('SuccessOutward/', views.SuccessOutward, name='SuccessOutward'),

    path('Admin_Dashboard/', views.Admin_Dashboard, name='Admin_Dashboard'),

    path('SavedDrafts/', views.SavedDrafts, name='SavedDrafts'),

    path('ProfilePage/', views.ProfilePage, name='ProfilePage'),

    path('Login2/', views.Login2, name='Login2'),

    path('SignUp2/', views.SignUp2, name='SignUp2'),

    path('DispatchForm4/', views.DispatchForm4, name='DispatchForm4'),

    path('PurchaseOrders/', views.PurchaseOrders, name='PurchaseOrders'),

    path('CollectionDash/ajax/objects.txt',views.ajax, name='ajax'),

    path('CollectionDashDetails/ajax/objects.txt',views.ajax, name='ajax'),


]