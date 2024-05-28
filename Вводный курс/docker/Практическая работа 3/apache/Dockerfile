FROM php:7.4-apache
RUN apt update
RUN apt install -y apache2
RUN apt install -y apache2-utils
RUN apt clean
COPY ./index.php /var/www/html
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
