FROM python:3

VOLUME /var/lib/django-db
ENV DATABASE_URL sqlite:////var/lib/django-db/schedule_db.sqlite

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN mkdir -p /home/schedule_editor && mkdir -p /home/schedule_editor/editor_lesson && mkdir -p /home/schedule_editor/schedule_editor

WORKDIR /home/schedule_editor

ADD requirements.txt /home/schedule_editor

RUN pip install -r /home/schedule_editor/requirements.txt

ADD schedule_editor /home/schedule_editor/schedule_editor

ADD editor_lesson /home/schedule_editor/editor_lesson

COPY manage.py /home/schedule_editor

#COPY schedule_db.sqlite3 /home/schedule_editor
