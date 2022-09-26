from rest_framework import serializers
from users.models import User
from ads.models import Ad, Comment

class CommentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Comment
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SlugRelatedField(
        source = 'author',
        queryset = User.objects.all(),
        slug_field = 'first_name',
    )
    
    author_last_name = serializers.SlugRelatedField(
        source = 'author',
        queryset = User.objects.all(),
        slug_field = 'last_name',
    )
    
    author_image = serializers.SerializerMethodField('get_author_image_url')
    
    class Meta:
        model = Comment
        fields = ['pk', 'text', 'created_at','author_id', 
                  'author_first_name', 'author_last_name',
                  'author_image', 'ad_id']
        
    def get_author_image_url(self, obj):
        request = self.context.get("request")
        image_url = obj.author.image.url if obj.author.image else '/django_media/user_images/4000x2500-beach-city.jpg'
        return request.build_absolute_uri(image_url)
    

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']
    
 
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
        
            
class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    phone = serializers.SlugRelatedField(
        source = 'author',
        queryset = User.objects.all(),
        slug_field = 'phone',
    )
    
    author_first_name = serializers.SlugRelatedField(
        source = 'author',
        queryset = User.objects.all(),
        slug_field = 'first_name',
    )
    
    author_last_name = serializers.SlugRelatedField(
        source = 'author',
        queryset = User.objects.all(),
        slug_field = 'last_name',
    )
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'phone', 'description',
                  'author_first_name', 'author_last_name', 'author_id']


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['image', 'title', 'price', 'description']