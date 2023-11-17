import docker
import sys

def check_container_health():
    client = docker.from_env()
    try:
        container = client.containers.get('nom_de_votre_conteneur')  # Remplacez 'nom_de_votre_conteneur' par le nom de votre conteneur
        if container.status == 'running':
            return 0
        else:
            return 1
    except docker.errors.NotFound:
        return 1
    except docker.errors.APIError:
        return 1

if __name__ == "__main__":
    sys.exit(check_container_health())
