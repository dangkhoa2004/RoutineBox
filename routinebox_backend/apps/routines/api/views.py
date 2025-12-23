from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.routines.services.sorting_engine import test_sorting_logic

class TestRoutineApi(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        message = test_sorting_logic()
        return Response({"status": "success", "message": message})