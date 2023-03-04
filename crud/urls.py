from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from dipendenti import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.getAll, name='index'),
    path('add/', views.addDipendenti, name= 'add'),
    path('upload/<int:id>', views.aggiornaDipendente),
    path('delete/<int:id>', views.delete)
]
