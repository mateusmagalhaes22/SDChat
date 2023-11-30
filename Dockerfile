FROM mysql:5.7

COPY ./dbconf/ /docker-entrypoint-initdb.d/

EXPOSE 3306