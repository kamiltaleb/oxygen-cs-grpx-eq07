## Pre-commit Git hook

Introduction

Dans le cadre de nos travaux de laboratoire sur l'intégration continue et le déploiement continu (CI/CD) pour le développement logiciel, nous avons mis en place un système de "hooks" de pré-commit. Ces "hooks" sont des scripts automatisés qui sont exécutés avant chaque engagement (commit) dans notre système de contrôle de version, Git. Ils sont configurés pour effectuer diverses vérifications de qualité de code et de cohérence afin d'améliorer l'efficacité de notre processus de développement. Voici une brève description de chaque hook configuré.

Pré-commit Hooks

Le premier hook provient du dépôt https://github.com/pre-commit/pre-commit-hooks. Il s'agit d'un ensemble de hooks de pré-commit créés par la communauté des développeurs. Dans notre configuration, nous utilisons le hook check-added-large-files. Celui-ci est conçu pour vérifier si de gros fichiers ont été ajoutés lors de l'engagement. L'objectif est d'éviter d'alourdir inutilement notre dépôt.

Le deuxième hook est pylint, provenant du dépôt https://github.com/pycqa/pylint. Pylint est un outil d'analyse de code source pour le langage de programmation Python. Dans notre configuration, nous avons désactivé toutes les vérifications par défaut (--disable=all) pour le moment.

Le troisième hook est black, provenant du dépôt https://github.com/psf/black. Black est un formatteur automatique pour le code Python qui suit une convention de style bien précise, ce qui favorise la lisibilité et la cohérence du code au sein de notre équipe.

Enfin, nous avons un hook local pytest. Pytest est un cadre de test pour Python que nous utilisons pour vérifier la validité de notre code. Cet hook est exécuté à partir d'un exécutable pytest dans notre environnement virtuel (.venv/Scripts/pytest.exe). Il est défini pour ne pas recevoir de noms de fichiers en entrée (pass_filenames: false), ce qui signifie qu'il exécute toujours la même commande, indépendamment des fichiers spécifiquement engagés.

Conclusion

L'utilisation des hooks de pré-commit nous permet de maintenir une certaine qualité de code et de prévenir les erreurs potentielles en intégrant ces vérifications au processus même d'engagement du code. Cela augmente l'efficacité de notre processus de développement et améliore la robustesse de notre code.
