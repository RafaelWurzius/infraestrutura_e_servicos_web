from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Configurações do banco de dados PostgreSQL
DB_USERNAME = 'postgres'
DB_PASSWORD = '1234'
DB_HOST = '192.168.15.2'
DB_PORT = '5432'
DB_NAME = 'infrauser'

# Cria uma instância do Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Cria uma instância do SQLAlchemy
db = SQLAlchemy(app)

# Modelo de dados - User
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Rota para inserir um novo usuário
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Dados incompletos'}), 400

    # Tenta criar um novo usuário
    new_user = User(username=username, password=password)
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'Failed to register user: {str(e)}'}), 500
    
# Rota para buscar um usuário pelo username
@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return jsonify({'status': 'success', 'message': 'Login successful!'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Login failed: Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(host='192.168.15.3', port=5000, debug=True)