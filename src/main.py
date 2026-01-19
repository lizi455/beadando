import os
import geopandas
import pandas

# Változók
INPUT_FILE = os.getenv("INPUT_FILE", "data/roads.geojson")
OUTPUT_GEOJSON = os.getenv("OUTPUT_GEOJSON", "results/roads_with_length.geojson")
OUTPUT_CSV = os.getenv("OUTPUT_CSV", "results/total_length.csv")

print("=== Road Network Analysis ===\n")

# Adatok beolvasása

print(f"Loading road network from: {INPUT_FILE}")
gdf = geopandas.read_file(INPUT_FILE)

print(f"Original CRS: {gdf.crs}")

# CRS ellenőrzése és szükség esetén átalakítás
if gdf.crs.to_string() == "EPSG:4326":
    print("Reprojecting to EPSG:3857 for accurate length calculation...")
    gdf = gdf.to_crs(epsg=3857)


# Úthosszak számítása minden útvonalnál
gdf["length_m"] = gdf.geometry.length


# Összesített hossz
total_length = gdf["length_m"].sum()

# Kimenetek mentése
# Részletek GeoJSON-ba
gdf.to_file(OUTPUT_GEOJSON, driver="GeoJSON")
print(f"Detailed road lengths saved to: {OUTPUT_GEOJSON}")


# Összesített érték CSV-be
pandas.DataFrame([{"total_road_length_m": total_length}]).to_csv(OUTPUT_CSV, index=False)
print(f"Total road length saved to: {OUTPUT_CSV}")

# Terminál output
print("\n=== Analysis Summary ===")
print(f"Number of road segments: {len(gdf)}")
print(f"Total road length: {total_length:.2f} meters")
print("=========================\n")
