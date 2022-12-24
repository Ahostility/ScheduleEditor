from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


class Schedule(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name,context)




class Authentication(TemplateView):

    template_name = 'auth.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name,context)

    # def post(self, response):


        # return JsonResponse({
        #     'method': 'GET'
        # })





























#
# def schedule(request):
#     if request.method == 'GET':
#         return JsonResponse({
#             'method': 'GET'
#         })
#
#     if request.method == 'POST':
#         uploadedFile = request.FILES["file"]
#
#         if uploadedFile != None:
#             fs = FileSystemStorage(location='files')
#             return JsonResponse({
#             'method': 'POST'
#             },status= 200)
#         else:
#             return JsonResponse({
#                 'message': 'Unexpected file field'
#                 }, status=500)
