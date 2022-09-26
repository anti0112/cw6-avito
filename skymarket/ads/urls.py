from django.urls import include, path
from ads.views import AdViewSet, CommentViewSet
from rest_framework.routers import SimpleRouter

ads_router = SimpleRouter()
ads_router.register('ads', AdViewSet, basename='ads')
ads_router.register('ads/(?P<ad_id>[^/.]+)/comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('', include(ads_router.urls))
]
