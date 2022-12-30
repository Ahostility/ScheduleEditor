from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SCHEDULE_DIR = BASE_DIR / "schedule_editor"
EDITOR_DIR = BASE_DIR / "editor_lesson"
TEMP_DIR = EDITOR_DIR / "templates"
STAT_DIR = EDITOR_DIR / "static"
DATA_DIR = STAT_DIR / 'data'
EXMPL_DIR = DATA_DIR / 'example'
SAVE_DIR = DATA_DIR / 'save'

if __name__ == '__main__':
    print(BASE_DIR)