import sqlite3
import uuid
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import ScheduleTable
from editor_lesson.create_doc import edit_document


class Schedule(TemplateView):
    template_name = 'index.html'

    key_db = ['csrfmiddlewaretoken', 'time_period', 'type_lesson',
              'name_lesson','group_name', 'cause',
              'science_degree_subject', 'job_subject','subject',
              'science_degree_object', 'job_object', 'object']

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
                {'title': 'Причина замены преподавателя',
                 'name': self.key_db[5],
                 'placeholder': "Текст"
                 }
            ],
            'subject_people': 'Инициатор замены',
            'object_people': 'Замещающий преподаватель',
            'title_since':'Научная степень инициатора',
            'list_since_su':[
                {'name': self.key_db[6],
                 'contains': " к.э.н."
                 },
                {'name': self.key_db[6],
                 'contains': "д.э.н."
                 },
                {'name': self.key_db[6],
                 'contains': "степень отсутствует"
                 }
            ],
            'list_job_su': [
                {'name': self.key_db[7],
                 'contains': "Заведующий кафедры"
                 },
                {'name': self.key_db[7],
                 'contains': "Профессор кафедры"
                 },
                {'name': self.key_db[7],
                 'contains': "Доцент кафедры"
                 },
                {'name': self.key_db[7],
                 'contains': "Ст. преподаватель"
                 },
                {'name': self.key_db[7],
                 'contains': "Ассистент"
                 },
            ],
            'list_people_su': [
                {'name': self.key_db[8],
                 'contains': "Щербаков Сергей Михайлович"
                 },
                {'name': self.key_db[8],
                 'contains': "Шполянская Ирина Юрьевна"
                 },
                {'name': self.key_db[8],
                 'contains': "Хубаев Георгий Николаевич"
                 },
                {'name': self.key_db[8],
                 'contains': "Долженко Алексей Иванович"
                 },
                {'name': self.key_db[8],
                 'contains': "Жебровская Людмила Анатольевна"
                 },
                {'name': self.key_db[8],
                 'contains': "Мирошниченко Ирина Иосифовна"
                 },
                {'name': self.key_db[8],
                 'contains': "Фрид Любовь Михайловна"
                 },
                {'name': self.key_db[8],
                 'contains': "Веретенникова Елена Григорьевна"
                 },
                {'name': self.key_db[8],
                 'contains': "Аручиди Наталья Александровна"
                 },
                {'name': self.key_db[8],
                 'contains': "Курбесов Александр Валерьянович"
                 },
                {'name': self.key_db[8],
                 'contains': "Прохорова Анна Михайловна"
                 },
                {'name': self.key_db[8],
                 'contains': "Данилова Татьяна Викторовна"
                 },
                {'name': self.key_db[8],
                 'contains': "Шкодина Татьяна Андреевна"
                 },
                {'name': self.key_db[8],
                 'contains': "Потапов Леонид Игоревич"
                 },
                {'name': self.key_db[8],
                 'contains': "Глушенко Сергей Андреевич"
                 },
                {'name': self.key_db[8],
                 'contains': "Гречкина Вера Юрьевна"
                 },
                {'name': self.key_db[8],
                 'contains': "Яковец Светлана Владимировна"
                 },
            ],
            'list_since_obj':[
                {'name': self.key_db[9],
                 'contains': " к.э.н."
                 },
                {'name': self.key_db[9],
                 'contains': "д.э.н."
                 },
                {'name': self.key_db[9],
                 'contains': "степень отсутствует"
                 }
            ],
            'list_job_obj': [
                {'name': self.key_db[10],
                 'contains': "Заведующий кафедры"
                 },
                {'name': self.key_db[10],
                 'contains': "Профессор кафедры"
                 },
                {'name': self.key_db[10],
                 'contains': "Доцент кафедры"
                 },
                {'name': self.key_db[10],
                 'contains': "Ст. преподаватель"
                 },
                {'name': self.key_db[10],
                 'contains': "Ассистент"
                 },
            ],
            'list_people_obj': [
                {'name': self.key_db[11],
                 'contains': "Щербаков Сергей Михайлович"
                 },
                {'name': self.key_db[11],
                 'contains': "Шполянская Ирина Юрьевна"
                 },
                {'name': self.key_db[11],
                 'contains': "Хубаев Георгий Николаевич"
                 },
                {'name': self.key_db[11],
                 'contains': "Долженко Алексей Иванович"
                 },
                {'name': self.key_db[11],
                 'contains': "Жебровская Людмила Анатольевна"
                 },
                {'name': self.key_db[11],
                 'contains': "Мирошниченко Ирина Иосифовна"
                 },
                {'name': self.key_db[11],
                 'contains': "Фрид Любовь Михайловна"
                 },
                {'name': self.key_db[11],
                 'contains': "Веретенникова Елена Григорьевна"
                 },
                {'name': self.key_db[11],
                 'contains': "АручидиНаталья Александровна"
                 },
                {'name': self.key_db[11],
                 'contains': "Курбесов Александр Валерьянович"
                 },
                {'name': self.key_db[11],
                 'contains': "Прохорова Анна Михайловна"
                 },
                {'name': self.key_db[11],
                 'contains': "Данилова Татьяна Викторовна"
                 },
                {'name': self.key_db[11],
                 'contains': "Шкодина Татьяна Андреевна"
                 },
                {'name': self.key_db[11],
                 'contains': "Потапов Леонид Игоревич"
                 },
                {'name': self.key_db[11],
                 'contains': "Глушенко Сергей Андреевич"
                 },
                {'name': self.key_db[11],
                 'contains': "Гречкина Вера Юрьевна"
                 },
                {'name': self.key_db[11],
                 'contains': "Яковец Светлана Владимировна"
                 },
            ]
        }
        return render(request, self.template_name, ctx)


    def post(self, request): # POST requset from page
        self.__save_request_to_db(request)
        data = dict(request.POST.dict())
        print(data)
        edit_document(data)
        return HttpResponseRedirect("statistic/")


    def __save_request_to_db(self, req) -> None: # Save data to db
        table_schedule = ScheduleTable()
        table_schedule.time_period = req.POST.get(self.key_db[1])
        table_schedule.type_lesson = req.POST.get(self.key_db[2])
        table_schedule.name_lesson = req.POST.get(self.key_db[3])
        table_schedule.group_name = req.POST.get(self.key_db[4])
        table_schedule.cause = req.POST.get(self.key_db[5])
        table_schedule.science_degree_subject = req.POST.get(self.key_db[6])
        table_schedule.job_subject = req.POST.get(self.key_db[7])
        table_schedule.subject = req.POST.get(self.key_db[8])
        table_schedule.science_degree_object = req.POST.get(self.key_db[9])
        table_schedule.job_object = req.POST.get(self.key_db[10])
        table_schedule.object = req.POST.get(self.key_db[11])
        table_schedule.save()


class Statistic(TemplateView):
    template_name = 'statistic.html'

    key_db = ['csrfmiddlewaretoken', 'subject', 'object']

    def get(self, request, *args, **kwargs): # Get auth of index page

        data = self._select_table() # создание вывода статистики
        stat = self._select_statistic(data.get(self.key_db[1]), data.get(self.key_db[2]))

        ctx = {
            'list_parm': [
                {'title':  "Замещаемый преподаватель",
                 'name': self.key_db[1],
                 'placeholder':  data.get(self.key_db[1]),
                 'number': len(stat[0])
                 },
                {'title': "Замещающий преподаватель",
                 'name': self.key_db[2],
                 'placeholder':  data.get(self.key_db[2]),
                 'number': len(stat[1])
                 }
            ]
        }
        return render(request, self.template_name, ctx)


    def post(self,request): # POST requset from page
        try:
            data = self._select_table()
            file = edit_document(data)
            bytes = open(file, 'rb')

            response = HttpResponse(bytes, content_type='application/docx')
            response['Content-Disposition'] = f"attachment; filename={uuid.uuid4()}.docx"
            return response
        except ValueError:
            return HttpResponseServerError(ValueError)

    def _select_table(self,):
        table_schedule = ScheduleTable.objects.get(id = ScheduleTable.objects.all().last().id)
        data_new = {
            'time_period':table_schedule.time_period,
            'type_lesson': table_schedule.type_lesson,
            'name_lesson':table_schedule.name_lesson,
            'group_name':table_schedule.group_name,
            'science_degree_subject':table_schedule.science_degree_subject,
            'job_subject':table_schedule.job_subject,
            'subject':table_schedule.subject,
            'science_degree_object':table_schedule.science_degree_object,
            'job_object':table_schedule.job_object,
            'object':table_schedule.object,
            'cause':table_schedule.cause
        }
        return data_new

    def _select_statistic(self,sbj,obj):
        subject_name = ScheduleTable.objects.filter(subject=sbj)
        object_name = ScheduleTable.objects.filter(object=obj)
        return subject_name,object_name




class Authentication(TemplateView):
    template_name = 'auth.html'

    def get(self, request, *args, **kwargs): # Get auth of index page
        context = {}
        # try:
        # data = dict(request.POST.dict())
        #
        #         file = edit_document(data)
        #         bytes = open(file, 'rb')
        #
        #         response = HttpResponse(bytes, content_type='application/docx')
        #         response['Content-Disposition'] = f"attachment; filename={uuid.uuid4()}.docx"
        #         return response
        #     except ValueError:
        #         return HttpResponseServerError(ValueError)

        return render(request, self.template_name, context)

if __name__ == '__main__':
    select = Statistic()
    print(select._select_table())
