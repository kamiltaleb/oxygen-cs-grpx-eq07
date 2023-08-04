# Stage 1: Construction des dépendances
FROM python:3.11.4-alpine AS builder

WORKDIR /build

# Copy only the dependency files and install the dependencies
COPY Pipfile* ./
RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --ignore-pipfile

# Stage 2: Image finale
FROM python:3.11.4-alpine

WORKDIR /app

# Copier les fichiers de l'étape précédente
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Install psycopg2 in the Python environment
RUN pip install psycopg2-binary

RUN sudo systemctl start postgresql

# Copy the application files
COPY . .

# Execute the application
CMD [ "python", "src/main.py" ]
