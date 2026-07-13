import csv
import json
with open("global_sales.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            row["quantity"] = float(row["quantity"])
            row["revenue"] = float(row["revenue"])
        except ValueError:
            row["quantity"] = 0
            row["revenue"] = 0





