import csv

with open('input_proxies.csv', 'r', encoding='utf8') as in_proxy:
    r = [i[0] for i in csv.reader(in_proxy)]
    print(r)