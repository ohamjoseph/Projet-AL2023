# Projet-AL2023
***
1. Après avoir cloné le projet déplacer vous dans le dossier **Projet-AL2023**
~~~bash
cd Projet-AL2023
~~~
et créér un environement python et installer les dépendances avec la commande :

~~~bash
> pip install -r requirements.txt
~~~

2. Ensuite lancer les trois serveurs Django
* D'abord **Delivery_api** sur le port _8000_

~~~bash
cd delivery_api
python manage.py runserver 8000
~~~

* Ensuite **Delivery_client** sur le port _8001_

~~~bash
cd delivery_client
python manage.py runserver 8001
~~~

* Enfin **Delevery_app** sur le port _8002_

~~~bash
cd delevery_app
python manage.py runserver 8002
~~~

3. Accéder à l'application client à l'adresse : ___127.0.0.1:8002___

---
