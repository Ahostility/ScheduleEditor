from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .models import ScheduleTable
from editor_lesson.create_doc import edit_document

from django.http import FileResponse
import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import os



class Schedule(TemplateView):

    template_name = 'index.html'

    key_db = ['csrfmiddlewaretoken', 'time_period', 'type_lesson', 'name_lesson',
              'group_name', 'science_degree_subject', 'surname_subject', 'name_subject',
              'parent_subject', 'science_degree_object', 'surname_object', 'name_object',
              'parent_object', 'cause']

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name,context)


    def post(self, request):
        # print(f"list: {request.POST.dict()}")
        # data = json.dumps(request.POST.dict(),indent=4)
        data = dict(request.POST.dict())
        print(self.key_db,data)
        file_path = edit_document(data)

        # self.__save_request_to_db(request)
        # self.__select_table()

        # responce = FileResponse(open(file_path,'rb'))
        return render(request, self.template_name,)


    def __save_request_to_db(self,req) -> None:
        table_schedule = ScheduleTable()
        table_schedule.time_period = req.POST.get(self.key_db[1])
        table_schedule.type_lesson = req.POST.get(self.key_db[2])
        table_schedule.name_lesson = req.POST.get(self.key_db[3])
        table_schedule.group_name = req.POST.get(self.key_db[4])
        table_schedule.science_degree_subject = req.POST.get(self.key_db[5])
        table_schedule.surname_subject = req.POST.get(self.key_db[6])
        table_schedule.name_subject = req.POST.get(self.key_db[7])
        table_schedule.parent_subject = req.POST.get(self.key_db[8])
        table_schedule.science_degree_object = req.POST.get(self.key_db[9])
        table_schedule.surname_object = req.POST.get(self.key_db[10])
        table_schedule.name_object = req.POST.get(self.key_db[11])
        table_schedule.parent_object = req.POST.get(self.key_db[12])
        table_schedule.cause = req.POST.get(self.key_db[13])
        table_schedule.save()
        pass


    def __select_table(self):
        # table_scgedule = ScheduleTable.objects.all()
        # print(table_scgedule.valuse())

        # time = dict(data)
        # print(data.)
        # schedule_table = ScheduleTable(
        #     time_period =
        #     type_lesson =
        #     name_lesson =
        #     group_name =
        #     science_degree_subject =
        #     surname_subject =
        #     name_subject =
        #     parent_subject =
        #     science_degree_object =
        #     surname_object =
        #     name_object =
        #     parent_object =
        #     cause =
        #     count_modified =
        # )
        pass


class Authentication(TemplateView):

    template_name = 'auth.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name,context)
