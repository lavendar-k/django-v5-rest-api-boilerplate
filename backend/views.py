from rest_framework.views import APIView
from rest_framework.response import Response


class UserView(APIView):
    def get(self, request):
        users = [
            {'name': "CodeMaster", 'age': 1},
            {'name': 'Luis', 'age': 2}
        ]
        return Response(users)

    def post(self, request):
        users = [
            {'name': "CodeMaster", 'age': 1},
            {'name': 'Luis', 'age': 2}
        ]
        return Response(users)
