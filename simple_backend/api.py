from simple_backend.models.colors import Colors
from simple_backend.serializers.colors import ColorsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ColorsList(APIView):
    """
    List all colors, or create a new color.
    """
    def get(self, request, format=None):
        colors = Colors.objects.all()
        serializer = ColorsSerializer(colors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ColorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
