-- Criar o banco de dados
CREATE DATABASE IF NOT EXISTS infrauser;

-- Conectar ao banco de dados
\c infrauser;

-- Criar tabela de usuários
CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username VARCHAR(80) UNIQUE NOT NULL, password VARCHAR(120) NOT NULL);

-- Inserir alguns dados de exemplo
INSERT INTO users (username, password) VALUES ('vanessa', '1234'), ('auti', '1234');
