from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


from .models import User
from .serializers import UserSerializer
from django.db.models import Q 

class CreateUserView(APIView):
    def post(self, request):
        if User.objects.filter(email=request.data.get('email')).exists():
            return Response({"error": "Usuário já existe com este email."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DeleteUserView(APIView):
    # permission_classes = [permissions.IsAuthenticated] 

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response({"message": "Usuário excluído com sucesso."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

class EditUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)

            # Verifica se o email ou username já existe, excluindo o usuário atual da verificação
            if request.data.get('email') and User.objects.filter(email=request.data.get('email')).exclude(id=user.id).exists():
                return Response({"error": "Email já existe."}, status=status.HTTP_400_BAD_REQUEST)

            if request.data.get('username') and User.objects.filter(username=request.data.get('username')).exclude(id=user.id).exists():
                return Response({"error": "Username já existe."}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    
class LoginView(APIView):
    def post(self, request):
        username_or_email = request.data.get('username_or_email')
        password = request.data.get('password')

        if not username_or_email:
            return Response({"error": "Nome de usuário ou e-mail não fornecido."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(Q(username=username_or_email) | Q(email=username_or_email)).first()

        if user is not None and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user)

            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
        
        if user is None:
            return Response({"error": "Usuário não existe!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Credenciais inválidas!"}, status=status.HTTP_401_UNAUTHORIZED)
        
class LogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logout bem-sucedido."}, status=status.HTTP_200_OK)

