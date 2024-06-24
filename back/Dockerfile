FROM python:3.9-slim

WORKDIR /app

# Instalar dependências
RUN pip install Flask flask_sqlalchemy SQLAlchemy psycopg2-binary

# Copiar arquivos da aplicação
COPY app/teste.py .
COPY app/app.py .

# Comando padrão para iniciar o backend
CMD ["python", "app.py"]
