# Criação de ambiente Django
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
 
# Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configurar o .gitignore antes das instruções seguintes

git init

# Sempre que fazer uma alteração nos arquivos, primeiro adiciona:
git add .
# Depois commita
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

# Por fim, faz o push para enviar os arquivos para o Github
git push origin main -u (Primeira vez)
"-u" permite que os push seguintes possam ser usadas apenas git push
git push (vezes seguintes)