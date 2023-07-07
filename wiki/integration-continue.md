## Mise en place d'un pipeline CI/CD

### Introduction

Dans le cadre de nos travaux de laboratoire, nous avons mis en place un pipeline d'Intégration Continue et de Déploiement Continue (CI/CD) afin d'améliorer l'efficacité de notre processus de développement logiciel. Ce pipeline est défini à l'aide de GitHub Actions, une plateforme d'automatisation qui permet de définir des workflows directement à partir de notre dépôt de code sur GitHub.

Configuration du pipeline CI/CD

Notre pipeline est déclenché à chaque fois qu'un développeur pousse (push) du code vers les branches main de notre dépôt. Il s'exécute sur une machine virtuelle Ubuntu fournie par GitHub Actions (runs-on: ubuntu-latest).

Il définit plusieurs variables d'environnement globales qui sont utilisées tout au long du pipeline. Celles-ci incluent les informations d'identification pour se connecter à une base de données MySQL locale et le nom de cette base de données.

Le pipeline est divisé en plusieurs "jobs", chacun accomplissant une tâche spécifique dans le processus de CI/CD. Voici une brève description de chaque job:

Checkout code: Ce job permet de récupérer le code source de notre dépôt.

Set up Python: Cette étape configure l'environnement Python sur la machine virtuelle.

Start MySQL service: Cette étape démarre le service MySQL sur la machine virtuelle.

Install MySQL client: Cette étape installe le client MySQL sur la machine virtuelle.

Set up Database: Cette étape se connecte à la base de données MySQL et crée une base de données et une table pour notre application.

Install dependencies: Cette étape installe les dépendances de notre application à partir d'un fichier requirements.txt à l'aide de pip, le gestionnaire de paquets Python.

Run unit tests: Cette étape exécute nos tests unitaires à l'aide de pytest, un framework pour Python.

Build Docker image: Cette étape construit une image Docker pour notre application à l'aide du fichier Dockerfile présent dans notre dépôt.

Publish Docker image: Enfin, cette étape se connecte à Docker Hub à l'aide d'un token d'authentification stocké en toute sécurité dans les secrets de GitHub et pousse notre image Docker à notre dépôt sur Docker Hub.

### Conclusion

En conclusion, l'implémentation d'un pipeline CI/CD nous a permis d'automatiser plusieurs aspects de notre processus de développement, notamment l'exécution de tests, la construction d'images Docker et la publication de ces images sur Docker Hub. Cela a amélioré l'efficacité de notre processus de développement et a permis une livraison plus rapide et plus fiable de notre application.
