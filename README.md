Ce repository a pour but de vous faire comprendre les mécanismes de construction d'une image Docker, de run de container et de diffusion d'image sur une registry.
On utilisera la ligne de commande afin d'être au plus proche du fonctionnement de Docker.

Ouvrez la documentation de docker : https://docs.docker.com/ elle est claire et efficace

## Initialisation du projet

- Cloner le repository en local
- Se placer dans le dossier du projet exemple bash
- Lire le fichier Dockerfile & le fichier script.sh
- Lancer la commande `docker build -t my-hello-world:0.1 .` afin de construire l'image docker
  - Ici le -t permet de nommer notre image et de lui donner un tag (ici 0.1), pensez à l'incrémenter à chaque modification de votre image
  - Le . permet de dire que le Dockerfile est dans le dossier courant
- Lancer la commande `docker run my-hello-world` afin de lancer le container


## Mon propre container

- Sur le principe du container précédent, créez un container qui affiche votre nom et prénom, en python, en partant de l'image python:3-alpine

**BONUS**
- Ajouter un argument à votre script python afin de pouvoir afficher le nom et prénom de votre choix
  - Faire en sorte que cet argument soit loadé depuis les variables d'environnement précisé lors du lancement du container (cf. `docker run -e`) (indice : check la doc de ARG & ENV dans le Dockerfile)
- Ajouter une library python de votre choix (ex: requests) et l'utiliser dans votre script python
- Faire boucler votre script indéfiniment
  - Rebuild votre image et relancer votre container en arrière plan (cf. `docker run -d`)
  - Vérifier qu'il tourne en arrière plan avec la commande `docker ps`
- Ajoutez un healthcheck à votre container (https://docs.docker.com/engine/reference/builder/#healthcheck)
  - vérifier que votre container est bien en bonne santé avec la commande `docker ps`


## Diffusion de votre container
- Créer un repo github **publique** et pusher votre Dockerfile, script python et autres fichiers nécessaires
- Créer votre image docker avec un tag de version (ex: 0.1)
- Pusher votre image sur la registry github :
  - Authentifier vous sur la registry github : https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-with-a-personal-access-token-classic
  - Pusher votre image sur la registry : https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#pushing-container-images
- Supprimer votre image en local : `docker rmi <image_name>`
- Récupérer votre image depuis la registry github : `docker pull <image_name>`, la lancer et vérifier que tout fonctionne
- Récupérer l'image de votre voisin.e et la lancer


## Pour aller plus loin
- Comprendre les bonnes pratique de construction d'image : https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- Lire la doc du nouveau builder buildkit : https://docs.docker.com/develop/develop-images/build_enhancements/