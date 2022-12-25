import uuid

import aspose.words as aw
import os
from docx import Document, shared
from docx.enum.style import WD_STYLE_TYPE


class EditDocSchedule():

    def __init__(self,req):
        self.req = req


    def _edit_document(self,):
        time = str(self.req.get('time_period')).split('-')

        dictionary = {'date': time[0],
                      'time_start': time[1],
                      'time_end': time[2],
                      'type_lesson': self.req.get('type_lesson'),
                      'name_lesson': self.req.get('name_lesson'),
                      'group_name': self.req.get('group_name'),
                      'science_degree_subject': self.req.get('science_degree_subject'),
                      'surname_subject': self.req.get('surname_subject'),
                      'name_subject': self.req.get('name_subject'),
                      'parent_subject': self.req.get('parent_subject'),
                      'science_degree_object': self.req.get('science_degree_object'),
                      'surname_object': self.req.get('surname_object'),
                      'name_object': self.req.get('name_object'),
                      'parent_object': self.req.get('parent_object'),
                      'cause': self.req.get('cause')
                      }

        doc = Document(r'C:\Users\Jfisto\Desktop\schedule_editor\editor_lesson\static\data\example\example.docx')
        for i in dictionary:
            for j in doc.paragraphs:
                if j.text.find(i) >= 0:
                    j.text = j.text.replace(i,dictionary[i])

        file_name = r'C:\Users\Jfisto\Desktop\schedule_editor\editor_lesson\static\data\save\file.docx'
        doc.save(file_name)
        return file_name


    def _delite_file(self):
        dir = 'C:\Users\Jfisto\Desktop\schedule_editor\editor_lesson\static\data\save'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        pass


def edit_document(req):
    edit = EditDocSchedule(req)
    edit._delite_file()
    edit._edit_document()

# 25.12.2022-10:15-12:00

if __name__ == '__main__':
    edit_document()