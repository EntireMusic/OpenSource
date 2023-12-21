import folium
import json
from collections import defaultdict
from folium.plugins import BeautifyIcon

with open('json_lines/KTP-271 L-3.json', encoding='utf8') as input_file:
    some_line = [i for i in json.load(input_file) if i.get('NOMER')]

# Координаты линии
coordinates = sorted(some_line, key=lambda x: x['NOMER'])

# Собираем отрезки линии в список (по номерам опор)
d = defaultdict(list)
for c in coordinates[1:]:
    d[c['OPORA_ZAD']] += [c['NOMER']]

# Создаём двойные координаты для отрезков
double_coordinates = []
for key, values in d.items():
    for v in values:
        double_coordinates.append((coordinates[key-1]['COORDS'], coordinates[v-1]['COORDS']))

# Вычисляем центральные координаты
center_lat = sum(c['COORDS'][0] for c in coordinates) / len(coordinates)
center_lon = sum(c['COORDS'][1] for c in coordinates) / len(coordinates)

# Создаем объект карты
my_map = folium.Map(location=[center_lat, center_lon], zoom_start=16)

# Инициализируем иконки
opr = '<div style="width: 8px; height: 8px; border: 2px solid black; background-color: white;"></div>'
tp = '<div style="width: 16px; height: 16px; border-radius: 50%; background-color: black;"></div>'

# Добавляем ТП на карту
folium.Marker(coordinates[0]['COORDS'], icon=folium.DivIcon(html=tp, icon_anchor=(10, 10))).add_to(my_map)

# Добавляем опоры на карту
for dot in coordinates[1:]:
    # Создаём иконки цифр
    num = BeautifyIcon(number=dot['NOMER'], background_color=False, border_color='rgba(0, 0, 0, 0)',
                       inner_icon_style='font-size:12px; padding-left:14px;')
    folium.Marker(dot['COORDS'], icon=folium.DivIcon(html=opr), number=1).add_to(my_map)
    folium.Marker(dot['COORDS'], icon=num).add_to(my_map)

# Добавляем пролёты на карту
for line in double_coordinates:
    folium.PolyLine(locations=line, weight=2, color='yellow').add_to(my_map)

# Сохраняем карту в HTML-файл
my_map.save('карта_линии.html')
