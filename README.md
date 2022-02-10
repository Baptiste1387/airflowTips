# airflowTips

## Security
- Il est possible de connecter ariflow à Vault, pour stocker les données sensibles
- On peut attribuer des droits aux utilisateurs
 - le Role "USER" permet de n'avoir accès qu'au DAG
 - on peut garder le role "OPS" pour les personnes devant créer des connexions SSH, API GKE ... ainsi les users peuvent utiliser ces connexions


## dagWithSS.py
Exemple d'un DAG qui permet de faire du SSH


## Kubernetes Operator
### Install Minikube
https://phoenixnap.com/kb/install-minikube-on-ubuntu

- Pour que airflow puisse joindre kubernetes qui est installé sur le host il faut ajouter cette ligne au niveau du docker-compose ????
