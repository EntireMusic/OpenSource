import os
import json
from pyproj import CRS, Transformer


def sk_to_wgs84(lat, lon):
    sk = CRS(f'epsg:7827')
    wgs84 = CRS('epsg:4326')

    transformer = Transformer.from_crs(sk, wgs84)
    x_wgs84, y_wgs84 = transformer.transform(lat, lon)
    return x_wgs84, y_wgs84


def get_lines():
    path = os.getcwd() + '\\lines\\'
    objects_list = os.listdir(path)

    for line_filename in objects_list:
        with (open(path + line_filename, encoding='cp1251') as line,
              open(f'json_lines\\{line_filename.split(".")[0]}.json', 'w', encoding='utf8') as out):
            out_line = []
            for obj in line.readlines():
                data = obj.strip().split(',')
                d = {}
                for k, v in [value.split(':') for value in data[5:]]:
                    try:
                        try:
                            d[k] = int(v)
                        except ValueError:
                            d[k] = float(v)
                    except ValueError:
                        d[k] = v

                d.update({'COORDS': sk_to_wgs84(data[1], data[2]), 'TYPE': data[4]})
                out_line.append(d)
            json.dump(out_line, out, ensure_ascii=False, indent='\t')


get_lines()
