import folium
import csv
data = []
with open('鄉鎮區發生車禍筆數.csv', 'r', newline='', encoding="utf-8") as infile:
    reader = csv.reader(infile)
    for row in reader:
        data.append(row)
        
map = folium.Map(location=[25.03949721583935, 121.55957402734612], tiles='OpenStreetMap', zoom_start=10)
for i in range(1, len(data)):
    folium.CircleMarker(
        location = [(data[i])[2],(data[i])[1]],
        popup = (data[i])[0],
        radius = (eval((data[i])[3])/150),
        color = '#c93756',
        fill = True,
        fill_color = '#c93756',
        weight = 2).add_to(map)
map.save("BubbleMap.html")