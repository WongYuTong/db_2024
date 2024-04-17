import geopandas as gpd
import pandas as pd
import folium
import os
os.environ['SHAPE_RESTORE_SHX'] = 'YES'
# 读取Shapefile文件
shapefile_path = "COUNTY_MOI_1090820.shp"
gdf = gpd.read_file(shapefile_path)
gdf.crs = "EPSG:4326"
# 检查CRS信息
if gdf.crs is not None:
    print("Shapefile文件已设置CRS:", gdf.crs)
else:
    print("Shapefile文件未设置CRS")

csv_file_url = "output10.csv"
state_data = pd.read_csv(csv_file_url)

m = folium.Map(location=[23.790020, 120.949723], zoom_start=7)

folium.Choropleth(
    geo_data=gdf,
    name="縣市區塊變色",
    data=state_data,
    columns=["id", "total"],
    key_on="properties.COUNTYID",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="發生車禍數量",
).add_to(m)
folium.LayerControl().add_to(m)
m.save("GeoPandasMap.html")


