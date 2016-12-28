#!/bin/bash
# 
# Extrae, reproyecta, fusiona y convierte a formato OSM fenómenos BTN25.
# Las hojas deberán estar como las deja descargaBTN25.sh,
# descomprimidas en carpetas según husos, por ejemplo:
# ./BTN25/Guipuzkoa/HUSO30/44011/
# 
# Santiago Crespo y Matías Taborda 2016 WTFL http://www.wtfpl.net/txt/copying/
# Es necesario tener la carpeta translations en el mismo sitio que btn252osm.sh

######## CONFIGURACIÓN ##########
# ¿Dónde tienes el BTN25?
DIRECTORIO_BTN25=/home/`whoami`/BTN25
######## FIN DE LA CONFIGURACIÓN ##########

LUGAR=$1
NOMBRE_IGN=$2
LETRA_PLURAL=S
NOMBRE_PROYECTO=$NOMBRE_IGN$LETRA_PLURAL-$LUGAR

if [ $# -ne 2 ] ; then
    echo "Uso: $0 Nombre-de-la-zona FENÓMENO-IGN"
    echo "Por ejemplo, si el directorio con las hojas es $DIRECTORIO_BTN25/Guipuzkoa"
    echo "y los archivos con el elemento tienen nombres como BTN25_ETRS_BCN0316S_LAGUNA_polygon.shp:"
    echo "$0 Guipuzkoa LAGUNA"
    exit 1
fi

if [ ! -f translations/$NOMBRE_IGN.py ]; then
    echo "ERROR! No encuentro la traducción que debería estar en translations/$NOMBRE_IGN.py"
    exit 1
fi

if [ ! -d $DIRECTORIO_BTN25/$LUGAR ]; then
    echo "ERROR! No encuentro el directorio $DIRECTORIO_BTN25/$LUGAR"
    echo "Configura la variable DIRECTORIO_BTN25 al principio del script"
    echo "o descarga los datos con descargaBTN25.sh."
    exit 1
fi

echo "## Copiando capas $NOMBRE_IGN..."
RUTA_INICIAL="`pwd`"
cd $DIRECTORIO_BTN25/$LUGAR
rm -rf /tmp/fusionar ; mkdir /tmp/fusionar
find | grep $NOMBRE_IGN | awk -F '/' '{print "cp ./"$2"/"$3"/"$4" /tmp/fusionar/"$2"_"$3"_"$4}' | sh

cd /tmp/fusionar
echo "## Fusionando shp según husos..."
for f in HUSO28*.shp; do ogr2ogr -update -append $NOMBRE_PROYECTO-huso28.shp $f -f "ESRI Shapefile" 2> /dev/null; done;
for f in HUSO29*.shp; do ogr2ogr -update -append $NOMBRE_PROYECTO-huso29.shp $f -f "ESRI Shapefile" 2> /dev/null; done;
for f in HUSO30*.shp; do ogr2ogr -update -append $NOMBRE_PROYECTO-huso30.shp $f -f "ESRI Shapefile" 2> /dev/null; done;
for f in HUSO31*.shp; do ogr2ogr -update -append $NOMBRE_PROYECTO-huso31.shp $f -f "ESRI Shapefile" 2> /dev/null; done;
rm HUSO* 2> /dev/null

echo "## Reproyectando coordenadas a EPSG:4326..."
[ -f $NOMBRE_PROYECTO-huso28.shp ] && ogr2ogr -s_srs "+init=epsg:25828 +wktext" -t_srs EPSG:4326 $NOMBRE_PROYECTO-4326_28.shp $NOMBRE_PROYECTO-huso28.shp
[ -f $NOMBRE_PROYECTO-huso29.shp ] && ogr2ogr -s_srs "+init=epsg:25829 +wktext" -t_srs EPSG:4326 $NOMBRE_PROYECTO-4326_29.shp $NOMBRE_PROYECTO-huso29.shp
[ -f $NOMBRE_PROYECTO-huso30.shp ] && ogr2ogr -s_srs "+init=epsg:25830 +wktext" -t_srs EPSG:4326 $NOMBRE_PROYECTO-4326_30.shp $NOMBRE_PROYECTO-huso30.shp
[ -f $NOMBRE_PROYECTO-huso31.shp ] && ogr2ogr -s_srs "+init=epsg:25831 +wktext" -t_srs EPSG:4326 $NOMBRE_PROYECTO-4326_31.shp $NOMBRE_PROYECTO-huso31.shp

echo "## Fusionando shp si hubiera varios husos..."
for f in $NOMBRE_PROYECTO-4326*.shp; do ogr2ogr -update -append $NOMBRE_PROYECTO-fusionado.shp $f -f "ESRI Shapefile"; done;

echo "## Convirtiendo codificación de caracteres de ISO-8859-15 a UTF-8..."
ogr2ogr -f "ESRI Shapefile" $NOMBRE_PROYECTO.shp -lco ENCODING=UTF-8 $NOMBRE_PROYECTO-fusionado.shp

echo "## Borrando archivos sobrantes..."
rm $NOMBRE_PROYECTO-*

echo "## Copiando archivos shp a $RUTA_INICIAL/$NOMBRE_PROYECTO/SHP..."
mkdir -p "$RUTA_INICIAL/$NOMBRE_PROYECTO/SHP"
cp /tmp/fusionar/* "$RUTA_INICIAL/$NOMBRE_PROYECTO/SHP"

echo "## Transformando $NOMBRE_PROYECTO.shp $NOMBRE_PROYECTO.osm..."
cd "$RUTA_INICIAL"
ogr2osm.py /tmp/fusionar/$NOMBRE_PROYECTO.shp -t $NOMBRE_IGN -o /tmp/fusionar/$NOMBRE_PROYECTO-NCR.osm &&  echo "## Convirtiendo NCR a UTF8..." && ascii2uni -a D /tmp/fusionar/$NOMBRE_PROYECTO-NCR.osm > "$RUTA_INICIAL/$NOMBRE_PROYECTO/$NOMBRE_PROYECTO.osm" && echo "## Creado $RUTA_INICIAL/$NOMBRE_PROYECTO/$NOMBRE_PROYECTO.osm :)" || { echo "## Error al transformar :("; exit 1; }
