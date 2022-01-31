# App level urls.py
from pages import views
urlpatterns = [
    path('', views.homepage_view,name='home'),
   
]