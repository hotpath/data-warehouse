load.zones <- function(shp.file) {
  require(sp)
  require(rgeos)
  require(maptools)
  
  zones <- list()
  
  crswgs84 <- sp::CRS('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
  
  shp <- maptools::readShapePoly(shp.file,
                                 proj4string = crswgs84,
                                 verbose = FALSE)
  
  zones.names <- data.frame(INDEX = as.numeric(rownames(shp@data[!is.na(shp@data$ZONA), ]))+1,
                            NAME = as.character(shp@data[!is.na(shp@data$ZONA), 'ZONA']))
  
  zones <- shp@polygons[zones.names$INDEX]
  
  rm(shp)
  
  zones <- lapply(zones, FUN = function(x) {
    return(slot(x, name = 'Polygons')[[1]])
  })
  
  names(zones) <- zones.names$NAME
  
  return(zones)
}

# Hay que cambiar el origen de coordenadas de la esquina superior izquierda a la esquina inferior izquierda, por lo que hay que modificar Y.
# El tamaño máximo en píxeles del mapa de cada planta es 1684, por lo que usaremos esta unidad para la transformación.
flip.coordinates <- function(zones, total.y = 1684) {
  if (!is.null(total.y)) {
    for (z in names(zones)) {
      zones[[z]]@coords[, 2] <- total.y-zones[[z]]@coords[, 2]
    }
  }
  return(zones)
}