FROM postgres:latest

# Variáveis de ambiente para configuração do PostgreSQL
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_DB=infrauser

# Copiar scripts SQL para diretório de inicialização do PostgreSQL
COPY init.sql /docker-entrypoint-initdb.d/
