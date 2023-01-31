import sqlite3
import uuid
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import ScheduleTable
from editor_lesson.create_doc import edit_document


class Schedule(TemplateView):
    template_name = 'index.html'
    template_name_rdct = 'index_red.html'

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
        self.__select_table()
        return render(request, self.template_name, ctx)


    def post(self, request): # POST requset from page
        self.__save_request_to_db(request)
        # self.__select_table()

        data = dict(request.POST.dict())
        edit_document(data)
        return HttpResponseRedirect("statistic/")


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
        print(table_schedule.name_subject)
        pass


    def __select_table(self): # Select data from table
        pass

        # try:
        #     sqlite_connection = sqlite3.connect(BASE_DIR / 'schedule_db.sqlite')
        #     cursor = sqlite_connection.cursor()
        #     print("Подключен к SQLite")
        #
        #     sqlite_select_query = f"""SELECT * from schedule_table"""
        #     cursor.execute(sqlite_select_query)
        #     print("Чтение одной строки \n")
        #     record = cursor.fetchall()
        #     print(f"count {cursor.rowcount")
        #     for row in record:
        #         print(row)
                # print("ID:", row[0])
                # print("Дата и время проведения занятия:", row[1])
                # print("Тип пары:", row[2])
                # print("Дисциплина:", row[3])
                # print("Имя группы:", row[4])
                # print("Научная степень инициатора:", row[5])
                # print("Фамилия инициатора замены", row[6])
                # print("Имя инициатора замены", row[7])
                # print("Отчество инициатора замены", row[8])
                # print("Научная степень замещающего преподавателя", row[9])
                # print("Фамилия замещающего преподавателя", row[10])
                # print("Имя замещающего преподавателя", row[11])
                # print("Отчество замещающего преподавателя", row[12])
                # print("Причина замены преподавателя", row[13])
                # print("Имя группы:", row[14])
            # cursor.close()
        #
        # except sqlite3.Error as error:
        #     print("Ошибка при работе с SQLite", error)
        # finally:
        #     if sqlite_connection:
        #         sqlite_connection.close()
        #         print("Соединение с SQLite закрыто")


class Statistic(TemplateView):
    template_name = 'statistic.html'

    key_db = ['csrfmiddlewaretoken', 'subject_name', 'object_name']

    def get(self, request, *args, **kwargs): # Get auth of index page
        ctx = {
            'list_parm': [
                {'title': 'Инициатор замены',
                 'name': self.key_db[1],
                 'placeholder': 10
                 },
                {'title': 'Замещающий перподавватель',
                 'name': self.key_db[2],
                 'placeholder': 12
                 }
            ]
        }
        return render(request, self.template_name, ctx)


    def post(self, request): # POST requset from page
        # try:
        self._select_table()
            # file = edit_document(data)
            # bytes = open(file, 'rb')

            # response = HttpResponse(bytes, content_type='application/docx')
            # response['Content-Disposition'] = f"attachment; filename={uuid.uuid4()}.docx"
            # return response
        # except ValueError:
        #     return HttpResponseServerError(ValueError)

    def _select_table(self):

        time_period = ScheduleTable.objects.get(pk=1)
        print(time_period)

        # table_schedule.time_period = req.POST.get(self.key_db[1])
        # table_schedule.type_lesson = req.POST.get(self.key_db[2])
        # table_schedule.name_lesson = req.POST.get(self.key_db[3])
        # table_schedule.group_name = req.POST.get(self.key_db[4])
        # table_schedule.science_degree_subject = req.POST.get(self.key_db[5])
        # table_schedule.surname_subject = req.POST.get(self.key_db[6])
        # table_schedule.name_subject = req.POST.get(self.key_db[7])
        # table_schedule.parent_subject = req.POST.get(self.key_db[8])
        # table_schedule.science_degree_object = req.POST.get(self.key_db[9])
        # table_schedule.surname_object = req.POST.get(self.key_db[10])
        # table_schedule.name_object = req.POST.get(self.key_db[11])
        # table_schedule.parent_object = req.POST.get(self.key_db[12])
        # table_schedule.cause = req.POST.get(self.key_db[13])
        # table_schedule.save()
        # print(table_schedule.name_subject)
        pass


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
