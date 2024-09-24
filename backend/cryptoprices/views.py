from rest_framework.views import APIView
from .serializers import CryptoPriceSerializer
from django.http.response import JsonResponse
from .models import CryptoPrice
from django.http.response import Http404
from rest_framework.response import Response


class CryptoPriceView(APIView):
    def get_cryptoprice(self, pk):
        try:
            cryptoprices = CryptoPrice.objects.all()[::pk]
            return cryptoprices
        except:
            return JsonResponse("CryptoPrice Does Not Exist", safe=False)

    def get(self, request, pk=None):
        interval = int(request.GET.get('interval', 1))
        data = CryptoPrice.objects.all()[::interval]
        serializer = CryptoPriceSerializer(data, many=True)
        # if pk:
        #     data = self.get_cryptoprice(pk)
        #     serializer = CryptoPriceSerializer(data)
        # else:
        #     data = CryptoPrice.objects.all()
        #     serializer = CryptoPriceSerializer(data, many=True)
        return Response(serializer.data)
    

    





