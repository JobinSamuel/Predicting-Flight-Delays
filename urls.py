
from django.contrib import admin
from django.urls import path
from FlightDelays import views as mainview
from users import views as usr
from admins import views as admins


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainview.index,name='index'),
    path('UserRegister/',mainview.UserRegister, name='UserRegister'),
    path('UserLogin/',mainview.UserLogin, name='UserLogin'),
    path('AdminLogin/', mainview.AdminLogin, name='AdminLogin'),
    path('Logout/', mainview.Logout, name='Logout'),

    ### User Based URLS
    path('UserRegisterAction/',usr.UserRegisterAction, name='UserRegisterAction'),
    path('UserLoginCheck/',usr.UserLoginCheck, name='UserLoginCheck'),
    path('UserUploadForm/', usr.UserUploadForm, name='UserUploadForm'),
    path('UserDataUpload/', usr.UserDataUpload, name='UserDataUpload'),
    path('DataPreProcessing/',usr.DataPreProcessing, name='DataPreProcessing'),
    path('UsermachineLearning/', usr.UsermachineLearning, name='UsermachineLearning'),
    path('UserGraphs/', usr.UserGraphs, name='UserGraphs'),

    ### Admin Based Urls
    path('AdminLoginCheck/',admins.AdminLoginCheck, name='AdminLoginCheck'),
    path('ViewUsers/', admins.ViewUsers, name='ViewUsers'),
    path('AdminActivaUsers/', admins.AdminActivaUsers, name='AdminActivaUsers'),
    path('AdmimnAddData/',admins.AdmimnAddData, name='AdmimnAddData'),
    path('AdminAddingFlightData/',admins.AdminAddingFlightData, name='AdminAddingFlightData'),
    path('AdminViewData/',admins.AdminViewData, name='AdminViewData'),
    path('AdminFindArrivalDelay/', admins.AdminFindArrivalDelay, name='AdminFindArrivalDelay'),
    path('AdminGraphs/',admins.AdminGraphs, name='AdminGraphs'),




]
