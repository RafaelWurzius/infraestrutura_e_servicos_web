from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do banco de dados PostgreSQL
#  'postgresql://postgres:1234@localhost:5432/infrauser'
DB_USERNAME = 'postgres'
DB_PASSWORD = '1234'
DB_HOST = '192.168.15.2' 
DB_PORT = '5432'
DB_NAME = 'infrauser'

# Cria a URI de conexão do SQLAlchemy
SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Cria uma instância do engine do SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)  # Defina echo=True para ver as queries SQL geradas

# Cria uma instância da sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Define a classe de modelo para a tabela 'users'
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

# Cria as tabelas no banco de dados (opcionalmente)
# Base.metadata.create_all(engine)

# Função para inserir um novo usuário
def insert_user(username, password):
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()
    print(f"Usuário '{username}' inserido com sucesso!")
    
# Função para buscar um usuário por nome de usuário
def get_user(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        print(f"Usuário encontrado - ID: {user.id}, Username: {user.username}, Password: {user.password}")
    else:
        print(f"Usuário '{username}' não encontrado.")

# Exemplo de utilização
if __name__ == '__main__':
    # Inserir um novo usuário
    insert_user('alice', 'password123')

    # Buscar um usuário
    get_user('alice')
