import csv
import json
with open("global_sales.csv","r",encoding="utf-8") as file:
    global_sales = csv.DictReader(file)
    for row in global_sales:
        try:
            row["quantity"] = float(row["quantity"])
            row["revenue"] = float(row["revenue"])
        except ValueError:
            row["quantity"] = 0
            row["revenue"] = 0
with open("regional_tariffs.json","r", encoding="utf-8") as json_file:
    regional_tariffs = json.load(json_file)
    for region, tariff in regional_tariffs.items():
        try:
            tariff = float(tariff)
        except ValueError:
            tariff = 0








