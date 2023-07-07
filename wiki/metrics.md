## Métriques d’intégration continue

En résumé, le choix de ces métriques d'intégration continue permet de surveiller et d'évaluer la performance, la stabilité, l'efficacité et la qualité du processus de build et des tests automatisés. Ces métriques fournissent des indicateurs clés pour mesurer l'amélioration continue et prendre des mesures correctives lorsque des problèmes sont identifiés.

1. Temps d’exécution du pipeline de build pour un build donné :
   Cette métrique calcule le temps nécessaire pour exécuter le build du pipeline à partir du temps à la fin que l'on soustraie au temps du démarrage. Nous l'avons choisis afin de déterminer les perfomances et l'efficacité du pipeline pour un build donné.

2. Temps moyen pour l'ensemble des builds pour une période donnée : Le temps moyen de build sur une période donnée permet de surveiller les tendances et de détecter les éventuels goulots d'étranglement ou problèmes de performance. Une augmentation du temps moyen de build peut indiquer des problèmes d'efficacité ou de configuration, et peut inciter à des actions correctives pour améliorer le processus de build.

3. Quantité de builds réussis et échoués : Cette métrique permet d'évaluer la stabilité et la fiabilité du processus de build. Enregistrer le nombre de builds réussis et échoués aide à identifier les problèmes fréquents, les tendances d'échec et à mesurer la qualité du code produit. Cela peut également aider à identifier les problèmes de dépendances, de configuration ou de compatibilité qui peuvent entraîner des échecs de build.

4. Quantité de tests automatisés réussis et échoués : Cette métrique fournit des informations sur la qualité des tests automatisés effectués lors du processus d'intégration continue. Le suivi du nombre de tests réussis et échoués permet d'identifier les problèmes de qualité, les dégradations de performances et les problèmes de compatibilité qui peuvent affecter le bon fonctionnement de l'application.

Toutes ces métriques seront implémentées dans `{kanbanMetrics}` dans le dossier metrics du TP1.
