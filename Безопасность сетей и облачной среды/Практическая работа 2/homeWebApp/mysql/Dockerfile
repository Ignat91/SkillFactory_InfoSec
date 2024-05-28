FROM mysql:5.7
ENV MYSQL_ROOT_USER=root
ENV MYSQL_ROOT_PASSWORD=2991
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password
ENV MYSQL_DATABASE=appDB
COPY ./dbfile /var/lib/mysql
COPY ./init.sql /docker-entrypoint-initdb.d
