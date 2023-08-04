# Stage 1: Construction des dépendances
FROM python:3.9-alpine AS builder

WORKDIR /build

# Copy only the dependency files and install the dependencies
COPY Pipfile* ./
RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --ignore-pipfile

# Stage 2: Image finale
FROM python:3.9-alpine

WORKDIR /app

# Copy the application files
COPY . .

# Execute the application
CMD [ "python", "src/main.py" ]
