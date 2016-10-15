# btn252osm
Extrae, reproyecta, fusiona y convierte a formato OSM fenómenos BTN25.

Este script sirve para facilitar la preparación de importaciones manuales de datos del BTN25 del IGN a OSM. **¡No subir los datos que genera directamente a OSM!**

Es necesario tener instalado [ogr2osm](https://github.com/pnorman/ogr2osm) y ogr2ogr (apt-get install gdal-bin)

Las hojas deberán estar como las deja [descargaBTN25.sh](https://github.com/kresp0/descargaBTN25), descomprimidas en carpetas según husos, por ejemplo:

./BTN25/Guipuzkoa/HUSO30/44011/

Uso: ./btn252osm.sh Nombre-de-la-zona FENÓMENO-IGN

Por ejemplo, si el directorio con las hojas es /home/usuario/BTN25/Guipuzkoa y los archivos con el elemento tienen nombres como BTN25_ETRS_BCN0316S_LAGUNA_polygon.shp:

./btn252osm.sh Guipuzkoa LAGUNA

Santiago Crespo y Matías Taborda 2016 WTFL http://www.wtfpl.net/txt/copying/
