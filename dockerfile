from mysql

COPY ./dbConf/ /docker-entrypoint-initdb.d/

EXPOSE 3306