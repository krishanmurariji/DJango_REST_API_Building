
from rest_framework import serializers
from .models import Todo
import re
from django.template.defaultfilters import slugify
class Todo_serializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()    
    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['title','discription','slug']
        excludes = ['created_at','updated_at']
    
    def get_slug(self, obj):
        return slugify(obj.title)
    
    def validate(self, validated_data):
        print(validated_data)
        if validated_data.get('title'):
            title = validated_data['title']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not regex.search(title) == None:
                raise serializers.ValidationError('title cannot contains special character')
        return validated_data

    def validate_title(self, data):
        if data:
            title = data
            if len(title)<3:
                raise serializers.ValidationError('title lenght cant be less than 3 char')
        return data