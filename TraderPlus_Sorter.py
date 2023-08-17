'''

This Python script is designed to read and organize pricing information from the TraderPlusPriceConfig.json file,
which is used in the DayZ Mod TraderPlus.
Mod Link: https://steamcommunity.com/sharedfiles/filedetails/?id=2458896948
The script arranges the pricing data in descending order, placing items with the highest buy price at the top.

'''
__author__ = "naps"
__copyright__ = "Copyright (C) 2023 Nick Shepherd"
__license__ = "General Public License v3.0"
__version__ = "1.0"

import os
import json

input_file = r"Path-to-your-TraderPlusPriceConfig" # Point towards your TraderPlusPriceConfig.json file.
output_file = os.path.join(os.path.dirname(input_file), "TraderPlusPriceConfig_sorted.json") # Output's to the same location as your input.

with open(input_file, "r") as f:
    data = json.load(f)

def sort_by_buy_price(product):
    return int(product.split(',')[-2]) # This should never change unless Dmitri changes it and screws us all.

for category in data["TraderCategories"]:
    category["Products"].sort(key=sort_by_buy_price, reverse=True)

with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

print(f"Sorted data written to {output_file}")
