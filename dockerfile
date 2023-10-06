from mysql:5.7

COPY ./dbConf/ /docker-entrypoint-initdb.d/

EXPOSE 3306