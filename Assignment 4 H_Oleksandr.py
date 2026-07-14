#1 Імпорт бібліотек та створення порожніх списків та словників
import csv
import json
import pandas as pd
import matplotlib.pyplot as plt
global_sales_new =[]
regional_tariffs_new = {}

#2 Прочитано файл "global_sales.csv",
# отримано назви стовпців та перетворено значення стовпців quantity та revenue на float тип
# додано чисті рядки в новий список словників
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

#3 Прочитано json файл, перетворено значення на float та додано в новий словник
with open("regional_tariffs.json","r", encoding="utf-8") as json_file:
    regional_tariffs = json.load(json_file)
    for region, tariff in regional_tariffs.items():
        try:
            tariff = float(tariff)
        except ValueError:
            tariff = 0
        regional_tariffs_new[region] = tariff

#4 Пораховано net profit використовуючи функцію
def calculate_net_profit(revenue, tariff):
    net_profit = revenue - (revenue * (tariff / 100))
    return net_profit

#5 Додано новий стовпець net profit з відповідними порахованими значеннями
for value in global_sales_new:
    region = value["region"]
    value["net_profit"] = calculate_net_profit(value["revenue"],regional_tariffs_new[region])

#6 Додано до net profit до змінної списку назв стовпців і записано чисті дані у новий файл cleaned_sales_updated.csv
headings.append("net_profit")
with open("cleaned_sales_updated.csv","w", newline ="") as file:
    writer = csv.DictWriter(file, fieldnames=headings)
    writer.writeheader()
    writer.writerows(global_sales_new)

#7 Пораховано net profit для кожної категорії та додано в новий словник
category_net_profit = {}
for transaction in global_sales_new:
    if transaction["product_category"] not in category_net_profit:
        category_net_profit[transaction["product_category"]] = 0
        category_net_profit[transaction["product_category"]] += transaction["net_profit"]
    else:
        category_net_profit[transaction["product_category"]] += transaction["net_profit"]

#8 Пораховано середній net profit по категоріям та відфільтровано категорії з профітом більшим за середній
average_net_profit_per_category = sum(category_net_profit.values()) / len(category_net_profit)
average_net_profit_per_category_filtered = {category:value for category,value in category_net_profit.items() if value > average_net_profit_per_category}

#9 Створено список словників з ключами category та net_profit та відфільтровано від більшого до меншого
average_net_profit_per_category_filtered_list = []
for key, value in average_net_profit_per_category_filtered.items():
    average_net_profit_per_category_filtered_list.append({"category":key,"net_profit":value})
average_net_profit_per_category_filtered_list.sort(key=lambda x: x["net_profit"], reverse=True)

#10 Записано список словників топ категорій у файл top_categories.json
with open("top_categories.json", "w", encoding="utf-8") as data:
    json.dump(average_net_profit_per_category_filtered_list, data, indent=4)

#11 Створено та виведено таблицю DataFrame для топ категорій
df = pd.DataFrame(average_net_profit_per_category_filtered_list)
print(df)

#12 Створено bar chart за допомогою matplotlib
df.plot(
    kind="bar",
    x="category",
    y="net_profit",
    title= "Top categories bar chart",
    legend = False
)
plt.ylabel("Net profit")
plt.show()










