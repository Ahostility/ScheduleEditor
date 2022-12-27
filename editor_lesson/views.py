import uuid
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.views.generic import TemplateView
from .models import ScheduleTable
from editor_lesson.create_doc import edit_document


class Schedule(TemplateView):
    template_name = 'index.html'

    key_db = ['csrfmiddlewaretoken', 'time_period', 'type_lesson', 'name_lesson',
              'group_name', 'science_degree_subject', 'surname_subject', 'name_subject',
              'parent_subject', 'science_degree_object', 'surname_object', 'name_object',
              'parent_object', 'cause']

    def get(self, request, *args, **kwargs): # Get page
        ctx = {
            'list_parm': [
                {'title': 'Дата и время проведения занятия',
                 'name': self.key_db[1],
                 'placeholder': "DD.MM.YYYY-hh:mm-hh:mm"
                 },
                {'title': 'Тип пары',
                 'name': self.key_db[2],
                 'placeholder': "Лек/Лаб"
                 },
                {'title': 'Дисциплина',
                 'name': self.key_db[3],
                 'placeholder': "Наименование"
                 },
                {'title': 'Имя группы',
                 'name': self.key_db[4],
                 'placeholder': "Группа(ы)"
                 },
                {'title': 'Научная степень инициатора',
                 'name': self.key_db[5],
                 'placeholder': "Сокращенно(проф.,д.э.н.)"
                 },
                {'title': 'Фамилия инициатора замены',
                 'name': self.key_db[6],
                 'placeholder': "Текст"
                 },
                {'title': 'Имя инициатора замены',
                 'name': self.key_db[7],
                 'placeholder': "Текст"
                 },
                {'title': 'Отчество инициатора замены',
                 'name': self.key_db[8],
                 'placeholder': "Текст"
                 },
                {'title': 'Научная степень замещающего преподавателя',
                 'name': self.key_db[9],
                 'placeholder': "Текст"
                 },
                {'title': 'Фамилия замещающего преподавателя',
                 'name': self.key_db[10],
                 'placeholder': "Текст"
                 },
                {'title': 'Имя замещающего преподавателя',
                 'name': self.key_db[11],
                 'placeholder': "Текст"
                 },
                {'title': 'Отчество замещающего преподавателя',
                 'name': self.key_db[12],
                 'placeholder': "Текст"
                 },
                {'title': 'Причина замены преподавателя',
                 'name': self.key_db[13],
                 'placeholder': "Текст"
                 }
            ]
        }
        return render(request, self.template_name, ctx)

    def post(self, request): # POST requset from page
        try:
            data = dict(request.POST.dict())

            file = edit_document(data)
            bytes = open(file, 'rb')

            response = HttpResponse(bytes, content_type='application/docx')
            response['Content-Disposition'] = f"attachment; filename={uuid.uuid4()}.docx"
            return response
        except ValueError:
            return HttpResponseServerError(ValueError)

    def __save_request_to_db(self, req) -> None: # Save data to db
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

    def __select_table(self): # Select data from table
        pass


class Authentication(TemplateView):
    template_name = 'auth.html'

    def get(self, request, *args, **kwargs): # Get auth of index page
        context = {}
        return render(request, self.template_name, context)
