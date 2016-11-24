import shapefile #Librería para manejar archivos shapefile
from shapely.geometry import Polygon #Librería para el manejo de figuras geométricas

# Aunque el formato shapefile es multifichero, el archivo que se ha de leer es el *.shp 
# El resto de los ficheros (*.shx  y *.dbf) deben de estar en la misma carpeta 
p0shp = shapefile.Reader('p0_vect_zonas_corners.shp')

# shapeRecords permite acceder a los polígonos y a los atributos de cada zona
for zone in p0shp.shapeRecords():
    print zone.record # lista de atributos [DN,ZONE,FLOOR]. El atribúto DN se puede omitir
    print shape # Información sobre la lista de puntos (POLYGON)
    poligono = Polygon(shape.points) # Creación de un polígono. Permite saber si un punto está dentro del polígono... etc.   
	
# Los polígonos que se obtienen a partir de los ficheros shapefile tienen el origen de coordenadas en la esquina superior izquierda, mientras que los puntos generados en el dataset tienen el origen en la esquina inferior izquierad
# Para convertir el origen de la esquina superior izquierda a la esquina inferior izquierda, simplemente hay que transformar Y con la función Y = 1684 - Y