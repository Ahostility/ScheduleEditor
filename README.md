cd ./schedule_editor/
docker build -t schedule_img .
#тегирование
docker tag schedule_img jfisto/schedule_img:1.2
#запуск контейнера
docker run -it --name SheduleUbuntu schedule_img
#Запуск контейнера с параметрами
docker run -d -p 8000:8000 --name RaspUbuntuServer --restart unless-stopped schedule_img python3 ./manage.py runserver 0.0.0.0:8000
