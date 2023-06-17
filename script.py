import pyproj

def coord_transformer(lon_min, lat_min, lon_max, lat_max):
    # Define the source and target coordinate systems
    target_crs = pyproj.CRS.from_epsg(102100)  # WKID 102100 (Projected Coordinate System)
    source_crs = pyproj.CRS.from_epsg(4326)    # WKID 4326 (Latitude-Longitude Coordinate System)

    # Create a transformer object for the conversion
    transformer = pyproj.Transformer.from_crs(source_crs, target_crs, always_xy=True)

    # Define the coordinates to transform
    # xmin = 74.75
    # ymin = 29.75
    # xmax = 75.25
    # ymax = 30

    # Perform the transformation
    x_min, y_min = transformer.transform(lon_min, lat_min)
    x_max, y_max = transformer.transform(lon_max, lat_max)

    # Print the transformed coordinates
    return (x_min, y_min, x_max, y_max)

lon_min = input("Enter minimum longitude: ")
lat_min = input("Enter minimum latitude: ")
lon_max = input("Enter maximum longitude: ")
lat_max = input("Enter maximum latitude: ")

coords = coord_transformer(lon_min, lat_min, lon_max, lat_max)

x_min, y_min, x_max, y_max = coords[0], coords[1], coords[2], coords[3]

url = "https://geoportal.nic.in/nicgis/rest/services/SCHOOLGIS/Schooldata/MapServer/0/query?f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry={\"xmin\":%f,\"ymin\":%f,\"xmax\":%f,\"ymax\":%f,\"spatialReference\":{\"wkid\":102100}}&geometryType=esriGeometryEnvelope&inSR=102100&outFields=*&outSR=102100&quantizationParameters={\"mode\":\"view\",\"originPosition\":\"upperLeft\",\"tolerance\":9.554628535634974,\"extent\":{\"xmin\":68.5015470000764,\"ymin\":6.8114540002900235,\"xmax\":97.02722199976724,\"ymax\":35.032117999820365,\"spatialReference\":{\"wkid\":4326,\"latestWkid\":4326}}}" % (x_min, y_min, x_max, y_max)

print(url)


