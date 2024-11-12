import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoJSON file
gdf = gpd.read_file('open_adm_kommunegraenser_view.json')

# Set the active geometry column
gdf = gdf.set_geometry('geometry')

# Ensure the coordinate reference system is set to EPSG:25832
gdf = gdf.set_crs(epsg=25832)

# Plot the data
plot = gdf.plot()

# plot.figure.savefig('polygon.png')
gdf.centroid.plot(ax=plot, color='red').figure.savefig('polygon_centroids.png')
plt.show()

print("Done")
