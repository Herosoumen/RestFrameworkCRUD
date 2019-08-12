from rest_framework import serializers,fields
from ..models import Address,Profile
from django.contrib.auth.models import User

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'





class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email')



class ProfileSerializer(serializers.ModelSerializer):
    usermodel = UserSerializer(read_only = True)
    permanent_address_city = AddressSerializer(many = True)
    class Meta:
        model = Profile
        fields = ['phone_number','gender','created_at','usermodel','permanent_address_city']

    def create(self,validated_data):
        addresses = validated_data.pop('permanent_address_city')
        address_create = Address.objects.create(**addresses)
        username = validated_data.pop('username')
        user_details = User.objects.get(username  = username)
        profile = Profile.objects.create(user = user_details,permanent_address_city = address_create,**validated_data)
        return profile
        # for validated in validated_data:
