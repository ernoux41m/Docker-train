FROM alpine:latest

# Copier le script bash dans le conteneur, à sa racine

COPY script.sh script-hello-world.sh

# Donner les permissions d'exécution au script

RUN chmod +x script-hello-world.sh

# Exécuter le script lors du lancement du conteneur

CMD ["/script-hello-world.sh"]