from django.conf.urls import url
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import routers

from policy import views


# router = routers.DefaultRouter()
# router.register(r'policies', views.PolicyViewSet, base_name='policies')

# urlpatterns = router.urls

urlpatterns = [
    url(r'^policy', views.PolicyView.as_view(), name='policy'),
]
