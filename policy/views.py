# from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response

from policy.serializers import PolicySerializer


class PolicyView(views.APIView):

    resource_name = 'policy'

    def post(self, request, format=None):
        serializer = PolicySerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)
