from django.db import IntegrityError
from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict


from .models import Account

# Create your views here.

class AccountView(APIView):
    
    def post(self, request: Request) -> Response:
        received_data = request.data
        try:
            new_acc = Account.objects.create(**received_data)
        except IntegrityError:
            return Response({'error': "email or passport already exist"}, status.HTTP_400_BAD_REQUEST)
        convert_acc = model_to_dict(new_acc)
        return Response({'msg': convert_acc }, status.HTTP_201_CREATED)
    
    def get(self, request: Request) -> Response:
        accounts = Account.objects.all()
        converted_acc = []
        
        data = [ 
                converted_acc.append(model_to_dict(account))
                for account in accounts
        ]
        return Response({"msg": converted_acc})
    
class AccountDetailView(APIView):
    def get(self, request: Request, account_id: int) -> Response:
        try:
            acc = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return Response({'error': 'there is no account with this id'}, status.HTTP_404_NOT_FOUND)
        convert_acc = model_to_dict(acc)
        return Response({'msg': convert_acc})
    
    def delete(self, request: Request, account_id: int) -> Response:
        try:
            acc = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return Response({'error': 'there is no account with no id'}, status.HTTP_404_NOT_FOUND)
        acc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request: Request, account_id: int) -> Response:
        try:
            acc = Account.objects.get(pk=account_id)
        except Account.DoesNotExist:
            return Response({'error': 'there is no account with this id'}, status.HTTP_404_NOT_FOUND)
        
        for key, value in request.data.items():
            setattr(acc, key, value)
        acc.save()    
        convert_acc = model_to_dict(acc)
        return Response(convert_acc)