cd C:\Users\Jfisto\Desktop\schedule_editor\
docker build -t schedule_img .
docker run -it --name SheduleUbuntu schedule_img
 docker run -d -p 8000:8000 --name RaspUbuntuServer schedule_img python3 ./manage.py runserver 0.0.0.0:8000