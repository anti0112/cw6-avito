from rest_framework import  viewsets
from ads.serializers import *
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from ads.filters import AdFilter


class AdViewSet(viewsets.ModelViewSet):
    
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    serializer_action_classes = {
        'list': AdListSerializer,
        'retrieve': AdDetailSerializer,
        'create': AdCreateSerializer,
        'update': AdCreateSerializer,
    }
    
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    @action(detail=False, methods=['get'], url_path=r'me', serializer_class=AdListSerializer)
    def user_ads(self, request, *args, **kwargs):
        current_user = self.request.user
        users_ads = Ad.objects.filter(author=current_user)
        page = self.paginate_queryset(users_ads)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
        
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
        
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment
    serializer_class = CommentSerializer
    serializer_action_classes = {
        'list': CommentListSerializer,
        'retrieve': CommentListSerializer,
        'create': CommentCreateSerializer,
        'update': CommentCreateSerializer,
    }

    def get_queryset(self):
        return Comment.objects.filter(ad_id = self.kwargs['ad_id'])
    
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
        
    def perform_create(self, serializer):
        ad = Ad.objects.get(pk=self.kwargs['ad_id'])
        serializer.save(author=self.request.user, ad=ad)
        