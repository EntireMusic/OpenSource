import folium
from folium.plugins import BeautifyIcon

# Координаты линии
coordinates = [[0, 0, (50.41421, 30.45369)], [1, 0, (50.41429, 30.45372)], [2, 1, (50.41434, 30.45382)], [3, 2, (50.41463, 30.45373)], [4, 3, (50.41495, 30.45363)], [5, 4, (50.41524, 30.45354)], [6, 5, (50.41553, 30.45344)], [7, 6, (50.41578, 30.45337)], [8, 7, (50.416, 30.4533)], [9, 8, (50.41622, 30.45324)], [10, 9, (50.41645, 30.45316)], [11, 10, (50.41668, 30.45308)], [12, 11, (50.41668, 30.45308)], [13, 12, (50.41708, 30.45335)], [14, 13, (50.41719, 30.45332)], [15, 13, (50.41719, 30.45365)], [16, 15, (50.4173, 30.45365)], [17, 16, (50.41733, 30.45364)], [18, 15, (50.41731, 30.45404)], [19, 18, (50.4174, 30.45399)], [20, 19, (50.41744, 30.45398)], [21, 19, (50.41748, 30.45417)], [22, 18, (50.41737, 30.45419)], [23, 22, (50.41747, 30.45452)], [24, 23, (50.41758, 30.45451)], [25, 23, (50.4175, 30.45459)], [26, 25, (50.41762, 30.45464)], [27, 25, (50.41759, 30.45491)], [28, 27, (50.41775, 30.45519)]]

coordinates = sorted(coordinates, key=lambda x: x[0])

# Собираем отрезки линии в список (по номерам опор)
d = {}
for c in coordinates[1:]:
    d[c[1]] = d.get(c[1], []) + [c[0]]

# Создаём двойные координаты для отрезков
double_coordinates = []
for key, values in d.items():
    for v in values:
        double_coordinates.append([coordinates[key][-1], coordinates[v][-1]])

# Вычисляем центральные координаты
center_lat = sum(c[-1][0] for c in coordinates) / len(coordinates)
center_lon = sum(c[-1][1] for c in coordinates) / len(coordinates)

# Создаем объект карты
my_map = folium.Map(location=[center_lat, center_lon], zoom_start=20)

# Добавляем опоры на карту
opr = '<div style="width: 10px; height: 10px; border: 2px solid black; background-color: white;"></div>'
tp = '<div style="width: 20px; height: 20px; border-radius: 50%; background-color: black;"></div>'
folium.Marker(coordinates[0][-1], icon=folium.DivIcon(html=tp, icon_anchor=(10, 10))).add_to(my_map)
for dot in coordinates[1:]:
    num = BeautifyIcon(number=dot[0], background_color=False, border_color='rgba(0, 0, 0, 0)',
                       inner_icon_style='font-size:14px; padding-left:16px;')
    folium.Marker(dot[-1], icon=folium.DivIcon(html=opr), number=1).add_to(my_map)
    folium.Marker(dot[-1], icon=num).add_to(my_map)

# Добавляем пролёты на карту
for line in double_coordinates:
    folium.PolyLine(locations=line, weight=2, color='yellow').add_to(my_map)

# Сохраняем карту в HTML-файл
my_map.save('карта_линии.html')
