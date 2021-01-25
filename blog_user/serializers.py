from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth import get_user_model


User = get_user_model()

class UserCreationSerializer(ModelSerializer):
    password2 = CharField(label='Confirm Password')
    class Meta:
        model = User
        fields = [
            'email', 'password', 'password2' ]
        extra_kwargs = {'password':{'write_only':True}}

    def validate_password2(self, value):
        data = self.get_initial()
        password2 = value
        password = data.get('password')
        if password != password2:
            raise ValidationError("Password and Confirm Password didn't match.")
        return value
    
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(email=email)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data