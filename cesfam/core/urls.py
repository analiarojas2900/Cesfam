
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [

    #registro
    path('', views.admin_creacion, name='admin_creacion'),
    path('registro',views.registro,name='registro'),
    path('login',views.login,name='login'),
    #farmaceutico
    path('menumedicamentos',views.menumedicamentos,name='menumedicamentos'),
    path('registromedicamento',views.registromedicamento,name='registromedicamento'),
    path('retiromedicamento',views.retiromedicamento,name='retiromedicamento'),
    path('stock',views.stock,name='stock'),
    path('menufarmaceutico',views.menufarmaceutico,name='menufarmaceutico'),
#medico
    path('ajustes',views.ajustes,name='ajustes'),
    path('buscar',views.buscar,name='buscar'),
    path('menu',views.menu,name='menu'),
    path('perfil',views.perfil,name='perfil'),
    path('menuprescripcion',views.menuprescripcion,name='menuprescripcion'),
    path('inventario',views.inventario,name='inventario'),
    path('menureserva',views.menureserva,name='menureserva'),
#paciente
    path('tomahora',views.tomahora,name='toma de hora'),
]

