from django.urls import path
from .views.guide_views import Guides, GuideDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('guides/', Guides.as_view(), name='guides'),
    path('guides/<int:pk>/', GuideDetail.as_view(), name='guide_detail'),
]
