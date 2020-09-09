from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from . models import ImageUpload
from . serializers import ImageSerializer


class ImageAPIView(APIView):
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        if pk:
            image = ImageUpload.objects.get(id=pk)
            data = {'id': image.id, 'image_name': image.image_name, 'image': image.image.path}
        else:
            images = ImageUpload.objects.all()

            data = []
            for image in images:
                temp = {'id': image.id, 'image_name': image.image_name, 'image': image.image.path}

                data.append(temp)

        return Response(data)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            message = "Save successful"
            status_code = status.HTTP_201_CREATED
        else:
            message = "Something went wrong."
            status_code = status.HTTP_400_BAD_REQUEST

        return Response({'message': message}, status=status_code)

