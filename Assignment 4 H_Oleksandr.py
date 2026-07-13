import csv
import json
global_sales_new =[]
regional_tariffs_new = {}

with open("global_sales.csv","r",encoding="utf-8") as file:
    global_sales = csv.DictReader(file)
    headings = global_sales.fieldnames
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


def calculate_net_profit(revenue, tariff):
    net_prift = revenue - (revenue * (tariff / 100))
    return net_prift


for value in global_sales_new:
    region = value["region"]
    value["net_profit"] = calculate_net_profit(value["revenue"],regional_tariffs_new[region])

headings.append("net_profit")
with open("cleaned_sales_updated.csv","w", newline ="") as file:
    writer = csv.DictWriter(file, fieldnames=headings)
    writer.writeheader()
    writer.writerows(global_sales_new)


category_net_profit = {}
for transaction in global_sales_new:
    if transaction["product_category"] not in category_net_profit:
        category_net_profit[transaction["product_category"]] = 0
        category_net_profit[transaction["product_category"]] += transaction["net_profit"]
    else:
        category_net_profit[transaction["product_category"]] += transaction["net_profit"]

average_net_profit_per_category = sum(category_net_profit.values()) / len(category_net_profit)
average_net_profit_per_category_filtered = {category:value for category,value in category_net_profit.items() if value > average_net_profit_per_category}










