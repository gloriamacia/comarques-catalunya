# comarques-catalunya
GeoJson de les comarques i províncies de Catalunya amb i sense capital de comarca. 

Dades obtingudes de l'idescat (https://www.idescat.cat) i open street maps (https://www.openstreetmap.org/) el 19/11/2021. Inclou el Moianès. 

Es presenta també el codi per generar les comarques i províncies a partir del qual es pot fàcilment actualitzar el repositori fent servir overpass turbo (https://overpass-turbo.eu/).

![image](https://user-images.githubusercontent.com/17580456/142721560-d5c336fb-36c8-43a0-b179-108b52bdd9e8.png)

La carpeta "idescat" conté dades obtingudes de l'idescat (https://www.idescat.cat) el 21/11/2021. Concretament: 
* https://www.idescat.cat/codis/?id=50&n=9
* https://www.idescat.cat/pub/?id=ist&lang=en
* https://www.idescat.cat/pub/?id=aec&n=925

Comarques de Catalunya i l'Aran. Quan l'IST no estava disponible a nivell de municipi, s'ha indicat com a valor que manca ("IST_idescat" = 0) i s'ha utilitzat el valor de la comarca com a substitut. El resultat final és el fitxer idescat_data_final.csv i s'ha generat amb el codi de Python idescat_data_preprocessing.ipynb.

Per visualitzar el mapa, cal instal.lar les llibreries indicades a requirements.txt. Després python -m flask run. 