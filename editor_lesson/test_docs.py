from docx import Document
from docx.shared import Pt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SCHEDULE_DIR = BASE_DIR / "schedule_editor"
EDITOR_DIR = BASE_DIR / "editor_lesson"
TEMP_DIR = EDITOR_DIR / "templates"
STAT_DIR = EDITOR_DIR / "static"
DATA_DIR = STAT_DIR / 'data'
EXMPL_DIR = DATA_DIR / 'example'
SAVE_DIR = DATA_DIR / 'save'

dictionary = {'date': 1,
                      'time_start': 1,
                      'time_end': 1,
                      'type_lesson': 1,
                      'name_lesson': 1,
                      'group_name': 1,
                      'science_degree_subject': 1,
                      'surname_subject': 1,
                      'name_subject': 1,
                      'parent_subject': 1,
                      'science_degree_object': 1,
                      'surname_object': 1,
                      'name_object': 1,
                      'parent_object': 1,
                      'cause': 1
                      }

doc = Document(EXMPL_DIR / 'example_parm.docx')
for j in doc.paragraphs:
    print(j[0])
    doc.save(SAVE_DIR / 'file.docx')

