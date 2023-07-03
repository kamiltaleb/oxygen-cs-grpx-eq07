# Utiliser une image de base Python 3.8
FROM python:3.8-slim-buster

RUN mkdir /app 
# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt dans le conteneur
COPY requirements.txt /app

# Installer les dépendances à l'aide de pip
RUN pip install -r /app/requirements.txt

# Copier le reste des fichiers de l'application dans le conteneur
COPY ../src/ /app

# Exécuter l'application
CMD [ "python", "./main.py" ]
