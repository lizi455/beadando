import os
import geopandas 

INPUT_FILE = os.getenv("INPUT_FILE", "data/roads.geojson")
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "results/roads_with_lenght.geojson")

print("Loading road network")
gdf = geopandas.read_file(INPUT_FILE)

print("Calculating road lenghts")
gdf["lenght_m"] = gdf.geometry.length
total_lenght = gdf["lenght_m"].sum()

print(f"Total road lenght: {total_lenght: .2f} meters")

print("Saving results")
gdf.to_file(OUTPUT_FILE, driver="GeoJSON")

print("Done")