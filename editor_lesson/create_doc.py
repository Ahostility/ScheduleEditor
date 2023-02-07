from docx import Document
from docx.shared import Pt
from .dirs import EXMPL_DIR, SAVE_DIR
from .create_date import DataRasp


class EditDocSchedule():

    def __init__(self,req):
        self.req = req


    def _edit_document(self,):
        date_lessons = DataRasp()
        date_start_end = date_lessons.sum_date(str(self.req.get('time_period')))
        day = date_start_end[0].split('-')
        subject = str(self.req.get('subject')).split(" ")
        object = str(self.req.get('object')).split(" ")

        dictionary = {'date': f"{day[2]}.{day[1]}.{day[0]}",
                      'time_start':date_start_end[1],
                      'time_end': date_start_end[2],
                      'type_lesson': self.req.get('type_lesson'),
                      'name_lesson': self.req.get('name_lesson'),
                      'group_name': self.req.get('group_name'),
                      'science_degree_subject': self.req.get('science_degree_subject'),
                      'surname_subject': subject[0],
                      'name_subject': subject[1][0],
                      'parent_subject': subject[2][0],
                      'science_degree_object': self.req.get('science_degree_object'),
                      'surname_object': object[0],
                      'name_object': object[1][0],
                      'parent_object': object[2][0],
                      'cause': self.req.get('cause')
                      }

        doc = Document(EXMPL_DIR / 'example.docx')
        # style = doc.styles['Normal']
        # style.font.name = 'Time New Roman'
        # style.font. size = Pt(16)
        for i in dictionary:
            for j in doc.paragraphs:
                # print(j[0])
                if j.text.find(i) >= 0:
                    j.text = j.text.replace(i,dictionary[i])

        doc.save(SAVE_DIR / 'file.docx')

        return SAVE_DIR / 'file.docx'


    # def _delite_file(self):
    #     dir = 'C:\Users\Jfisto\Desktop\schedule_editor\editor_lesson\static\data\save'
    #     for f in os.listdir(dir):
    #         os.remove(os.path.join(dir, f))
    #     pass


def edit_document(req):
    edit = EditDocSchedule(req)
    # edit._delite_file()
    return edit._edit_document()

# 25.12.2022-10:15-12:00

# if __name__ == '__main__':
#     edit_document()