FROM php:7.4-apache

WORKDIR /var/www/html

# Copiar arquivos da aplicação

COPY app/home.php .
COPY app/index.php .
COPY app/login.php .
COPY app/register.php .
COPY app/registrar.php .
COPY app/style.css .
COPY app/user.jpg .


# Comando padrão para iniciar o backend
CMD ["php", "-S", "0.0.0.0:8000"]