from django.urls import path
from .views import Home
from .views import RegisterUser
from .views import RegisterAdmin
from .views import DinningPlaceList
from .views import search

urlpatterns = [
    path('', Home.as_view()),
    path('register/', RegisterUser.as_view()),
    path('registeradmin/', RegisterAdmin.as_view()),
    path('diningplace/', DinningPlaceList.as_view()),
    path('search/', search.as_view())
]