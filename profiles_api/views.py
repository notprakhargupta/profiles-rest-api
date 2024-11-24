from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):

    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_api_view = [
            "Uses HTTP methods as functions (GET, POST, PATCH, PUT, DELETE)",
            "Is similar to a traditional Django view",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs",
        ]

        return Response({
            "message": "Hello!",
            "an_api_view": an_api_view
        })