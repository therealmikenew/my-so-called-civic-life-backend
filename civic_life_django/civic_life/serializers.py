from rest_framework import serializers
from .models import User, Legislation, Action


class UserSerializer(serializers.HyperlinkedModelSerializer):
    legislations = serializers.HyperlinkedRelatedField(
        view_name='legislation_detail',
        many=True,
        read_only=True
    )
    actions = serializers.HyperlinkedRelatedField(
        view_name='action_detail',
        many=True,
        read_only=True
    )

    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail'
    )

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'profile_URL',
                  'street_address', 'city', 'state', 'zip_code', 'legislations', 'actions', 'user_url')


class LegislationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user'
    )

    legislation_url = serializers.ModelSerializer.serializer_url_field(
        view_name='legislation_detail'
    )

    class Meta:
        model = Legislation
        fields = ('id', 'title', 'bill_number', 'summary', 'url',
                  'sponsor', 'cosponsor', 'date_introduced', 'user', 'user_id', 'legislation_url')


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user'
    )

    action_url = serializers.ModelSerializer.serializer_url_field(
        view_name='action_detail'
    )

    class Meta:
        model = Action
        fields = ('id', 'date', 'description', 'notes',
                  'completed', 'user', 'user_id', 'action_url')
