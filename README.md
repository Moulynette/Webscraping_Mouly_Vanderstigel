# Webscraping_Mouly_Vanderstigel
Ce projet montre des techniques de scraping basé sur les outils Selenium et BeautifulSoup. Nous nous intéressons à la diversité des catégories de vêtements ainsi qu'à l'évolution des prix de deux grands sites de vente.

Vous trouverez un notebook pour chaque site expliquant les méthodes employées et un fichier python illustrant notre API Web.

Nous voulions ajouter d'autres sites à notre base de donnée mais nous avons rencontré des difficultés peu après la présentation du projet en classe. C'est un problème qui a été recensé par plusieurs élèves qui avaient recours à google colab. L'intêret initial d'utiliser colab plutôt que des ressources en local était de s'affranchir des limites en nombre de requête avec une adresse IP dynamique. Cependant depuis plus d'une semaine, google semble avoir modifié l'utilisation du driver avec selenium rendant impossible le chargement du module chrome ou firefox.

Nous avons donc finalement trouvé une technique peu commode (voir le notebook booho_scraping) qui consiste à créer un fichier python depuis l'espace de stockage de google colab et d'executer le module de selenium dans le script depuis une seule cellule colab. 

Cette méthode est évidement très pénible puisqu'elle complique énormément le process de debug en nous obligeant à coder et tester depuis un objet string.

Voici le lien des deux sites : 

https://fr.shein.com/

https://fr.boohoo.com/


Pour utiliser l'API, il suffit de lancer le script en local:

1-Ouvrir un invité de commande et se placer dans le répertoire du code
2-pip install "uvicorn[standard]"  
3-pip install fastapi   
4-python -m uvicorn api:app --reload
5-Se rednre sur : http://127.0.0.1:8000/docs pour visualiser nos use cases 
