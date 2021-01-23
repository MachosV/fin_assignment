from django.urls import path,include

from . import views
from api import views as APIviews


urlpatterns = [
    path('test', views.TestTemplate.as_view(), name='TestTemplate'),
    path('logout', views.LogoutView.as_view(), name='LogoutView'),
    path('login', views.LoginTemplate.as_view(), name='LoginTemplate'),
    path('api/budget', APIviews.MockAPIView, name="MockAPIView"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]