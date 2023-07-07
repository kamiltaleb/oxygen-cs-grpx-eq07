## Test

L'environnement de test utilié est unittest qui est déja intégré dans python. L'essenble des tests
se retrouve dans le dossier test du projet.

1. Pour lancer seulement les test unitaire, il suffit une commande `py test_main.py` au niveau du dossier de test. Un résumé sera affiché dans la console pour les tests qui ont réussis et pour les tests qui ont échoués.

2. Les test seront aussi lancer automatiquement durant le pré-commit. Si il y a une erreur dans les test unitaires, le commit sera annulé.

3. Finalement les tests seront aussi lancé durant le build de l'image docker du projet. Si il y a une erreur, le build va s'arrêter. Voir dans le fichier docker.md pour avoir accèes aux images de projet.
