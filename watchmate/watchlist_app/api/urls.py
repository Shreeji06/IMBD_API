from pathlib import Path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList1, ReviewDetail, ReviewCreate, StreamPlatformVS
from watchlist_app.api.views import UserReview, watchlist
# from watchmate.watchlist_app.models import WatchList

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [

    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('list2/', watchlist.as_view(), name='watch-list'),
    path('', include(router.urls)),
    #     path('stream/', StreamPlatformAV.as_view(), name='stream'),
    #     path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(),
    #     name='streamplatform-detail'),
    # path('review/', ReviewList1.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-list'),
    path('<int:pk>/review-create/',
         ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/',
         ReviewList1.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('reviews/', UserReview.as_view(),
         name='user-review-detail'),

]
