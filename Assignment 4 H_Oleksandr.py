import csv
import json
global_sales_new =[]
regional_tariffs_new = {}
with open("global_sales.csv","r",encoding="utf-8") as file:
    global_sales = csv.DictReader(file)
    for row in global_sales:
        try:
            row["quantity"] = float(row["quantity"])
        except ValueError:
            row["quantity"] = 0
        try:
            row["revenue"] = float(row["revenue"])
        except ValueError:
            row["revenue"] = 0
        global_sales_new.append(row)
with open("regional_tariffs.json","r", encoding="utf-8") as json_file:
    regional_tariffs = json.load(json_file)
    for region, tariff in regional_tariffs.items():
        try:
            tariff = float(tariff)
        except ValueError:
            tariff = 0
        regional_tariffs_new[region] = tariff
print(global_sales_new)
print(regional_tariffs_new)








