from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.guide import Guide
from ..serializers import GuideSerializer, UserSerializer


class Guides(generics.ListCreateAPIView):
    permission_classes_by_method = {
        'GET': (),
        'POST': (IsAuthenticated,),
    }
    serializer_class = GuideSerializer
    def get(self, request):
        """Index request"""
        guides = Guide.objects.all()
        # Run the data through the serializer
        data = GuideSerializer(guides, many=True).data
        return Response({ 'guides': data })

    def post(self, request):
        """Create request"""
        request.data['guide']['owner'] = request.user.id

        guide = GuideSerializer(data=request.data)
        if guide.is_valid():
            guide.save()
            return Response({ 'guide': guide.data }, status=status.HTTP_201_CREATED)
        return Response(guide.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        print(self.request.method)
        try:
            return [permission() for permission in self.permission_classes_by_method[self.request.method]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

class GuideDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        guide = get_object_or_404(Guide, pk=pk)
        if not request.user.id == guide.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this guide')

        data = GuideSerializer(guide).data
        return Response({ 'guide': data })

    def delete(self, request, pk):
        """Delete request"""
        guide = get_object_or_404(Guide, pk=pk)
        if not request.user.id == guide.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this guide')
        guide.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        if request.data['guide'].get('owner', False):
            del request.data['guide']['owner']

        guide = get_object_or_404(Guide, pk=pk)

        if not request.user.id == guide.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this guide')

        request.data['guide']['owner'] = request.user.id

        data = GuideSerializer(guide, data=request.data)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
