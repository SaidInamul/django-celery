pip freeze > requirements.txt
chmod +x ./entrypoint.sh
http://localhost:8001
docker exec -it django /bin/sh
./manage.py shell
./manage.py startapp newapp
docker-compose up -d --build django redis celery celery2
