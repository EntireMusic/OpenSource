import folium

coordinates = [
    [0, None, (48.55050, 37.66750)],
    [1, 0, (48.55010, 37.66748)],
    [5, 4, (48.54850, 37.66740)],
    [2, 1, (48.54970, 37.66746)],
    [3, 2, (48.54930, 37.66744)],
    [6, 1, (48.55025, 37.66784)],
    [4, 3, (48.54890, 37.66742)],
    [7, 6, (48.55019, 37.66857)]
]

coordinates = sorted(coordinates, key=lambda x: x[0])

# Собираем отрезки линии в список
d = {}
for c in coordinates[1:]:
    d[c[1]] = d.get(c[1], []) + [c[0]]

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
opr = '<div style="width: 10px; height: 10px; border: 2px solid black;"></div>'
tp = ('<div style="width: 0; height: 0; border-left: 15px solid transparent; border-right: 15px solid transparent;'
      'border-bottom: 25px solid black; position: relative; right: 80%; bottom: 100%;"></div>')
folium.Marker(coordinates[0][-1], icon=folium.DivIcon(html=tp)).add_to(my_map)
for dot in coordinates[1:]:
    folium.Marker(dot[-1], icon=folium.DivIcon(html=opr)).add_to(my_map)

# Добавляем пролёты на карту
for line in double_coordinates:
    folium.PolyLine(locations=line, color='yellow').add_to(my_map)

# Сохраняем карту в HTML-файл
my_map.save('карта_линии.html')
