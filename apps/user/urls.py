# django
from django.urls import path, include
# third
# own
from apps.user.views import Logout

urlpatterns = [
    path('seller/', include(('apps.user.urls_seller', 'seller'))),
    path('buyer/', include(('apps.user.urls_buyer', 'buyer'))),
    path('logout/', Logout.as_view(), name='logout')
]