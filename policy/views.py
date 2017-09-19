# from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response

from policy.serializers import PolicySerializer


# class PolicyViewSet(viewsets.ViewSet):

#     resource_name = 'policy'
#     serializer_class = PolicySerializer

#     def get_serializer(self):
#         return PolicySerializer()

#     # def create(self, request):
#     #     return Response()

#     # def list(self, request):
#     #     return Response()

#     # def list(self, request):
#     #     serializer = PolicySerializer(instance=policies.values(), many=True)
#     #     return Response(serializer.data)


class PolicyView(views.APIView):

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
