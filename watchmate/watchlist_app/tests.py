

from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from watchlist_app.api import serializers
from watchlist_app import models
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class StreamPlatformTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="example1", password="password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(
            name="Netflix ",
            about=" #1 streaming platform ",
            website=" https://www.netflix.com "
        )

    def test_streamplatform_create(self):

        data = {
            "name": "netflix",
            "about": "no.1 streaming platform",
            "website": "http://www.netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(
            reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        response = self.client.get(
            reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WatchListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="example", password="password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(
            name="Netflix ",
            about=" #1 streaming platform ",
            website=" https://www.netflix.com "
        )

        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Example Movie",
                                                         storyline="Example Movie", active=True)

    def test_watchlist_create(self):
        data = {
            "platform": self.stream,
            "title": "Example Movie",
            "storyline": "Example Story",
            "active": True
        }
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_ind(self):
        response = self.client.get(
            reverse('movie-detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, 'Example Movie')


class ReviewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="example", password="password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix ",
                                                           about=" #1 streaming platform",
                                                           website=" https://www.netflix.com ")
        # self.stream2 = models.StreamPlatform.objects.create(name="Netflix ",
        # about=" #1 streaming platform ",
        # website=" https://www.netflix.com ")
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Example Movie",
                                                         storyline="Example Movie", active=True)

        self.watchlist2 = models.WatchList.objects.create(platform=self.stream, title="Example Movie",
                                                          storyline="Example Movie", active=True)

        self.review = models.ReviewList.objects.create(
            review_user=self.user, rating=5, descriptions="good one", watchlist=self.watchlist2,  active=True)

    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "descriptions": "Great movie!",
            "watchlist": self.watchlist,
            "active": True,
        }
        print(self.user)

        response = self.client.post(
            reverse('review-create', args=(self.watchlist.id,)),  data)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("data")
        self.assertEqual(models.ReviewList.objects.count(), 2)

        response = self.client.post(
            reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_create_unauth(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "descriptions": "great",
            "watchlist": self.watchlist,
            "active": True
        }

        self.client.force_authenticate(user=None)
        response = self.client.post(
            reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            "review_user": self.user,
            "rating": 4,
            "descriptions": "great-updated",
            "watchlist": self.watchlist,
            "active": False
        }
        response = self.client.put(
            reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(
            reverse('review-list', args=(self.watchlist.id,)),)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_ind(self):
        response = self.client.get(
            reverse('review-detail', args=(self.review.id,)),)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
