import os
import csv
import pyproj


def utm_to_wgs84(lat, lon):
    # # Создаём проекции UTM и WGS84
    # utm = pyproj.Proj(init='epsg:3857')
    # wgs84 = pyproj.Proj(init='epsg:4326')
    # # Преобразуем координаты из UTM в WGS84
    # x, y = pyproj.transform(utm, wgs84, lat, lon)
    # return round(x, 6), round(y, 6)
    x = int(int(lat)/1.1065637903775778)/100000
    y = int(int(lon)/1.1031351660296553)/100000
    return x, y


path = os.getcwd()+'\\lines\\'
objects_list = os.listdir(path)

d = []
with open(path+objects_list[-1], encoding='cp1251') as file:
    print(objects_list[-1])
    r = csv.reader(file)
    for line in r:
        if 'SPZH' not in line:
            for element in line:
                if element.startswith('NOMER'):
                    num = element.split(':')[-1]
                if element.startswith('OPORA_ZAD'):
                    last_num = element.split(':')[-1]
                    break
            lat, lon = utm_to_wgs84(float(line[1]), float(line[2]))
            d.append([int(num), int(last_num), (lat, lon)])
    print(d)
