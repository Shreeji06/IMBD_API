
from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform
from watchlist_app.models import ReviewList


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ReviewList
        exclude = ('watchlist',)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):

    # len_class = serializers.SerializerMethodField()

    # def get_len_name(self, object):
    # return len(object.title)

    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList
        fields = "__all__"


# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    # WatchList = WatchListSerializer(
        # many=True, read_only=True)

class StreamPlatformSerializer(serializers.ModelSerializer):
    WatchList = WatchListSerializer(many=True, read_only=True)
    # WatchList = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:

        model = StreamPlatform
        fields = "__all__"
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError(
    #             "Title and description should be different !")
    #     else:
    #         return data

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("name is too short")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 "title and description should be different")
#         else:
#             return data

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("name is toot short")
    #     else:
    #         return value
