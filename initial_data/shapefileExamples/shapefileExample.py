import shapefile #Librer�a para manejar archivos shapefile
from shapely.geometry import Polygon #Librer�a para el manejo de figuras geom�tricas

# Aunque el formato shapefile es multifichero, el archivo que se ha de leer es el *.shp 
# El resto de los ficheros (*.shx  y *.dbf) deben de estar en la misma carpeta 
p0shp = shapefile.Reader('p0_vect_zonas_corners.shp')

# shapeRecords permite acceder a los pol�gonos y a los atributos de cada zona
for zone in p0shp.shapeRecords():
    print zone.record # lista de atributos [DN,ZONE,FLOOR]. El atrib�to DN se puede omitir
    print shape # Informaci�n sobre la lista de puntos (POLYGON)
    poligono = Polygon(shape.points) # Creaci�n de un pol�gono. Permite saber si un punto est� dentro del pol�gono... etc.   
	
# Los pol�gonos que se obtienen a partir de los ficheros shapefile tienen el origen de coordenadas en la esquina superior izquierda, mientras que los puntos generados en el dataset tienen el origen en la esquina inferior izquierad
# Para convertir el origen de la esquina superior izquierda a la esquina inferior izquierda, simplemente hay que transformar Y con la funci�n Y = 1684 - Y