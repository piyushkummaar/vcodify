from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import *


urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('careers', Apply.as_view(), name='apply'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<pk>/', PortfolioDetailView.as_view(),name='project_detail'),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)