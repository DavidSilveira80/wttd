from django.contrib import admin
from django.urls import path
import eventex.core.views
from eventex.subscriptions.views import subscribe

urlpatterns = [
    path('', eventex.core.views.home),
    path('admin/', admin.site.urls),
    path('existe/', eventex.core.views.existe, name='existe'),
    path('inscricao/', subscribe),

]
