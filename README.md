# Comarques de Catalunya

GeoJson de les comarques i províncies de Catalunya amb i sense capital de comarca. 

Dades obtingudes de [l'idescat](https://www.idescat.cat) i [open street maps](https://www.openstreetmap.org/) el 19/11/2021. Inclou el Moianès. 

![image](https://user-images.githubusercontent.com/17580456/145862417-753e9bcb-4f5e-4345-a883-f0fecc6a6a8c.png)

Si només estàs buscant els polígons geojson de les comarques i províncies de Catalunya, les carpetes `amb-capital` i `sense-capital` és tot el que necessites i pots parar de llegir aquí. 

A continuació, també es presenta també el codi per generar les comarques i províncies a partir del qual es pot fàcilment actualitzar el repositori fent servir [overpass turbo](https://overpass-turbo.eu/).

![image](https://user-images.githubusercontent.com/17580456/142721560-d5c336fb-36c8-43a0-b179-108b52bdd9e8.png)

### Dades de l'Idescat

La carpeta "idescat" conté dades obtingudes de [l'idescat](https://www.idescat.cat) el 21/11/2021. Concretament: 
* https://www.idescat.cat/codis/?id=50&n=9
* https://www.idescat.cat/pub/?id=ist&lang=en
* https://www.idescat.cat/pub/?id=aec&n=925

Comarques de Catalunya i l'Aran. Quan l'IST no estava disponible a nivell de municipi, s'ha indicat com a valor que manca (`IST_idescat = 0`) i s'ha utilitzat el valor de la comarca com a substitut. El resultat final és el fitxer idescat_data_final.csv i s'ha generat amb el codi de Python `idescat/idescat_data_preprocessing.ipynb`.

### Farmàcies de Catalunya amb dades de CatSalut

Com a example d'ús, es visualitzen sobre el mapa les +3000 farmàcies de Catalunya, obtingudes de [CatSalut](https://salutweb.gencat.cat/ca/ambits_actuacio/per_perfils/empreses_i_establiments/oficines_de_farmacia/farmacies/) i geolocalitzades amb el codi de Python `catsalut/geocode_pharmacies.ipynb`

Per visualitzar el mapa en local, cal instal.lar les llibreries indicades a `requirements.txt`. Després `python -m flask run`. 

El map també es pot veure online, clicant a aquest enllaç https://farmacies-catalunya.herokuapp.com/ sense instal.lar res.

![image](https://user-images.githubusercontent.com/17580456/146636973-0b208a5b-24f3-4634-a79b-ac26667bfc82.png)
