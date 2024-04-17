import geopandas as gpd
shapefile_path = "COUNTY_MOI_1090820.shp"
gdf = gpd.read_file(shapefile_path, encoding='utf-8')
df = gdf[['COUNTYID', 'COUNTYNAME']]
csv_filename = "county_data.csv"
df.to_csv(csv_filename, index=False, encoding='utf-8')

