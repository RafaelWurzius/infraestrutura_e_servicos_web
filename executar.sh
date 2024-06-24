#Remover os containeres:
sudo docker rm -f my_postgres meu_backend meu_frontend

#Remover as imagens:
sudo docker rmi -f frontend-php backend-python postgresql

#Executar o ansible:
sudo ansible-playbook playbook.yml