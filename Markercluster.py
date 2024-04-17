import folium
from folium.plugins import MarkerCluster
import csv
fmap = folium.Map(location=[25.041858, 121.525618], zoom_start=10)
marker_cluster = MarkerCluster().add_to(fmap)
i = 0

with open("車禍地點.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        i+=1   
        latitude = float(row[-1])
        longitude = float(row[-2])  
        folium.Marker(location=[latitude, longitude], popup=row[2],icon=folium.Icon(color="red")).add_to(marker_cluster)
        print(i)
        if i == 100:
            break
print("儲存地圖")
fmap.save('map_with_cluster.html')
print("结束")
