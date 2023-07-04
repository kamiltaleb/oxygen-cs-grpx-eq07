# Stage 1: Construction des dépendances
FROM python:3.8-alpine AS builder

WORKDIR /build

# Copier uniquement les fichiers de dépendances et installer les dépendances
COPY Pipfile* ./
RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --ignore-pipfile

# Stage 2: Image finale
FROM python:3.8-slim-buster

WORKDIR /app

# Copier les fichiers de l'étape précédente
COPY --from=builder /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copier le reste des fichiers de l'application
COPY . .

# Exécuter l'application
CMD [ "python", "src/main.py" ]
