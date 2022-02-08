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

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'profile_URL',
                  'street_address', 'city', 'state', 'zip_code', 'legislations', 'actions')


class LegislationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user'
    )

    class Meta:
        model = Legislation
        fields = ('id', 'title', 'bill_number', 'summary', 'url',
                  'sponsor', 'cosponsor', 'date_introduced', 'user', 'user_id')


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user'
    )

    class Meta:
        model = Action
        fields = ('id', 'date', 'description', 'notes',
                  'completed', 'user', 'user_id')
