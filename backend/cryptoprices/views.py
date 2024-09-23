from rest_framework.views import APIView
from .serializers import CryptoPriceSerializer
from django.http.response import JsonResponse
from .models import CryptoPrice
from django.http.response import Http404
from rest_framework.response import Response


class CryptoPriceView(APIView):
    def get_cryptoprice(self, pk):
        try:
            cryptoprice = CryptoPrice.objects.get(rowId=pk)
            return cryptoprice
        except:
            return JsonResponse("CryptoPrice Does Not Exist", safe=False)

    def get(self, request, pk=None):
        if pk:
            data = self.get_cryptoprice(pk)
            serializer = CryptoPriceSerializer(data)
        else:
            data = CryptoPrice.objects.all()
            serializer = CryptoPriceSerializer(data, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     data = request.data
    #     serializer = CryptoPriceSerializer(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse("Student Created Successfully", safe=False)
    #     return JsonResponse("Failed to Add Student", safe=False)

    # def put(self, request, pk=None):
    #     student_to_update = CryptoPrice.objects.get(rowId=pk)
    #     serializer = CryptoPriceSerializer(instance=student_to_update, data=request.data, partial=True)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse("Student Updated Successfully", safe=False)
    #     return JsonResponse("Failed to Update Student")

    # def delete(self, request, pk=None):
    #     student_to_delete = CryptoPrice.objects.get(rowId=pk)
    #     student_to_delete.delete()
    #     return JsonResponse("Student Deleted Successfully", safe=False)





