from django.urls import path
from . import views

urlpatterns = [
    #Các trang chính
    path('', views.myIndex, name = 'index_1'),
    path('lichTrinh', views.lichTrinh, name = 'index_2'),
    path('login', views.login, name = 'index_3'),

    path('carsvexe', views.carsvexe, name = 'carsvexe'),
    path('addvexe', views.addvexe, name = 'addvexe'),
    path('carslist', views.carslist, name = 'carslist'),
    path('addcar', views.addcar, name = 'addcar'),
    
    path('chart', views.chart, name = 'chart'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    
    
    path('updatecar/<int:id>', views.updatecar, name = 'updatecar'),
    path('deletecar/<int:id>', views.deletecar, name = 'deletecar'),
    path('updatevexe/<int:id>', views.updatevexe, name = 'updatevexe'),
]
