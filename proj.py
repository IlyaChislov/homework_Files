import os

def func_res(data_list):
    cook_book = {}
    name_dishes = []
    count_ingredients = []
    other_data = []
    ingredients = []
    for data in data_list:
        name_dishes.append(data[0])
        count_ingredients.append(int(data[1]))
        other_data.append(data[2:])
    for data in other_data:
        for i in data:
            ingredients.append(i.split(" | "))
    for dishes in name_dishes:
        cook_book[dishes] = []
    count = 0
    for key, value in cook_book.items():
        for i in range(0, count_ingredients[count]):
            buf = {'ingredients_name': ingredients[i][0], 'quantity': ingredients[i][1], 'measure': ingredients[i][2]}
            value.append(buf)
        count += 1
    return cook_book

with open('recipes.txt', encoding="utf-8") as f:
    data_list=[]
    list_buf=[]
    for line in f:
        line=line.strip()
        if line!="":
            list_buf.append(line)
        else:
            data_list.append(list_buf)
            list_buf=[]

print(func_res(data_list))









