#! 2-a:
def orden(item):
   return item['name']


from Consumo_api import get_data_sw_character

sw_data = get_data_sw_character()

sw_data.sort(key=orden)

for index, character in enumerate(sw_data):
    print( character['name'], character['height'],len(character['films']))

#!2-b: 

from Consumo_api import filtrado 
 
sw_data = filtrado() 

for character in sw_data: 
    if character["name"].startswith("D" or "C") or character["name"].endswith("s"):
        print(character["name"])
