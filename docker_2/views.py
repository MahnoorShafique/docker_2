from django.http import JsonResponse
from django.views import View


class HomeView(View):

   def get(self, request):
      return JsonResponse({"message":
                           'what is this behaviourc efefewqf',
                           "status": "true"})
