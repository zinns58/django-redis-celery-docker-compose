# django-nginx-docker-compose

## require
1. 프로젝트 환경설정 파일 생성
> touch project/.env

2. .env 환경설정 파일 작성   
SECRET_KEY={SECRET_KEY}   
DB_HOST={DB_HOST}   
DB_NAME={DB_NAME}   
DB_PORT={DB_PORT}   
DB_USER={DB_USER}   
DB_PASSWORD={DB_PASSWORD}   

## only deploy mode : redis, celery in docker-compose
1. docker build & up   
> docker-compose up --build   

2. test   
http://localhost:8082/post/