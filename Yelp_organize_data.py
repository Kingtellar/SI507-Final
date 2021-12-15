import requests
import json
import webbrowser

import argparse
import pprint
import sys
import urllib

from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode
################################################################################
with open("Yelp_Combined.json") as f:
    data = json.load(f)

#print(i)

################################################################################
pickup_list = [[],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
delivery_list = [[],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
other_list = [[],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
List1 = [[], [], []]
List1[0] = pickup_list # List[0] is for pickup
List1[1] = delivery_list # List[1] is for delivery
List1[2] = other_list # List[2] is for others
#List1 = [pickup_list, delivery_list, other_list]

if len(data)==0:
    List1 = List1
else:
    for restaurant in data:
        title_list = []
        if "transactions" in restaurant and "pickup" in restaurant["transactions"]:
            pickup_list[0].append(restaurant)
            for style in restaurant["categories"]:
                title_list.append(style["title"])
            if "Sanwitches" in title_list:
                pickup_list[1][0].append(restaurant) #List[#][1] for 'Sandwitch'
                if "price" in restaurant and restaurant["price"] == "$":
                    pickup_list[1][1].append(restaurant) #List[#][#][1] for '$'
                if "price" in restaurant and restaurant["price"] == "$$":
                    pickup_list[1][2].append(restaurant) #List[#][#][2] for '$$'
                if "price" in restaurant and restaurant["price"] == "$$$":
                    pickup_list[1][3].append(restaurant) #List[#][#][3] for '$$$'
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    pickup_list[1][4].append(restaurant) #List[#][#][4] for '$$$$'
                if "price" not in restaurant:
                    pickup_list[1][5].append(restaurant) #List[#][#][5] for no price
            if "Pizza" in title_list:
                pickup_list[2][0].append(restaurant) #List[#][2] for 'Pizza'
                if "price" in restaurant and restaurant["price"] == "$":
                    pickup_list[2][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    pickup_list[2][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    pickup_list[2][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    pickup_list[2][4].append(restaurant)
                if "price" not in restaurant:
                    pickup_list[2][5].append(restaurant)
            if "Burgers" in title_list:
                pickup_list[3][0].append(restaurant) #List[#][3] for 'Burgers'
                if "price" in restaurant and restaurant["price"] == "$":
                    pickup_list[3][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    pickup_list[3][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    pickup_list[3][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    pickup_list[3][4].append(restaurant)
                if "price" not in restaurant:
                    pickup_list[3][5].append(restaurant)
            if "Parks" in title_list:
                pickup_list[4][0].append(restaurant) #List[#][4] for 'Parks'
                if "price" in restaurant and restaurant["price"] == "$":
                    pickup_list[4][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    pickup_list[4][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    pickup_list[4][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    pickup_list[4][4].append(restaurant)
                if "price" not in restaurant:
                    pickup_list[4][5].append(restaurant)
            if "Mexican" in title_list:
                pickup_list[5][0].append(restaurant) #List[#][5] for 'Mexican'
                if "price" in restaurant and restaurant["price"] == "$":
                    pickup_list[5][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    pickup_list[5][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    pickup_list[5][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    pickup_list[5][4].append(restaurant)
                if "price" not in restaurant:
                    pickup_list[5][5].append(restaurant)
            if "Desserts" in title_list:
                pickup_list[6][0].append(restaurant) #List[#][6] for 'Desserts'
                if "price" in restaurant and restaurant["price"] == "$":
                    pickup_list[6][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    pickup_list[6][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    pickup_list[6][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    pickup_list[6][4].append(restaurant)
                if "price" not in restaurant:
                    pickup_list[6][5].append(restaurant)
            if "Bars" in title_list:
                pickup_list[7][0].append(restaurant) #List[#][7] for 'Bars'
                if "price" in restaurant and restaurant["price"] == "$":
                    pickup_list[7][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    pickup_list[7][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    pickup_list[7][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    pickup_list[7][4].append(restaurant)
                if "price" not in restaurant:
                    pickup_list[7][5].append(restaurant)
            if "Salad" in title_list:
                pickup_list[8][0].append(restaurant) #List[#][8] for 'Salad'
                if "price" in restaurant and restaurant["price"] == "$":
                    pickup_list[8][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    pickup_list[8][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    pickup_list[8][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    pickup_list[8][4].append(restaurant)
                if "price" not in restaurant:
                    pickup_list[8][5].append(restaurant)
            if "Chinese" in title_list:
                pickup_list[9][0].append(restaurant) #List[#][9] for 'Chinese'
                if "price" in restaurant and restaurant["price"] == "$":
                    pickup_list[9][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    pickup_list[9][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    pickup_list[9][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    pickup_list[9][4].append(restaurant)
                if "price" not in restaurant:
                    pickup_list[9][5].append(restaurant)
            if "Bakeries" in title_list:
                pickup_list[10][0].append(restaurant) #List[#][10] for 'Bakeries'
                if "price" in restaurant and restaurant["price"] == "$":
                    pickup_list[10][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    pickup_list[10][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    pickup_list[10][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    pickup_list[10][4].append(restaurant)
                if "price" not in restaurant:
                    pickup_list[10][5].append(restaurant)
            if "Sanwitches" not in title_list and "Pizza" not in title_list and "Burgers" not in title_list and "Parks" not in title_list and "Mexican" not in title_list and "Desserts" not in title_list and "Bars" not in title_list and "Salad" not in title_list and "Chinese" not in title_list and "Bakeries" not in title_list:
                pickup_list[11][0].append(restaurant) #List[#][11] for 'others'
                if "price" in restaurant and restaurant["price"] == "$":
                    pickup_list[11][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    pickup_list[11][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    pickup_list[11][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    pickup_list[11][4].append(restaurant)
                if "price" not in restaurant:
                    pickup_list[11][5].append(restaurant)

        if "transactions" in restaurant and "delivery" in restaurant["transactions"]:
            delivery_list[0].append(restaurant)
            for style in restaurant["categories"]:
                title_list.append(style["title"])
            if "Sanwitches" in title_list:
                delivery_list[1][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    delivery_list[1][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    delivery_list[1][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    delivery_list[1][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    delivery_list[1][4].append(restaurant)
                if "price" not in restaurant:
                    delivery_list[1][5].append(restaurant)
            if "Pizza" in title_list:
                delivery_list[2][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    delivery_list[2][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    delivery_list[2][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    delivery_list[2][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    delivery_list[2][4].append(restaurant)
                if "price" not in restaurant:
                    delivery_list[2][5].append(restaurant)
            if "Burgers" in title_list:
                delivery_list[3][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    delivery_list[3][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    delivery_list[3][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    delivery_list[3][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    delivery_list[3][4].append(restaurant)
                if "price" not in restaurant:
                    delivery_list[3][5].append(restaurant)
            if "Parks" in title_list:
                delivery_list[4][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    delivery_list[4][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    delivery_list[4][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    delivery_list[4][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    delivery_list[4][4].append(restaurant)
                if "price" not in restaurant:
                    delivery_list[4][5].append(restaurant)
            if "Mexican" in title_list:
                delivery_list[5][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    delivery_list[5][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    delivery_list[5][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    delivery_list[5][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    delivery_list[5][4].append(restaurant)
                if "price" not in restaurant:
                    delivery_list[5][5].append(restaurant)
            if "Desserts" in title_list:
                delivery_list[6][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    delivery_list[6][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    delivery_list[6][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    delivery_list[6][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    delivery_list[6][4].append(restaurant)
                if "price" not in restaurant:
                    delivery_list[6][5].append(restaurant)
            if "Bars" in title_list:
                delivery_list[7][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    delivery_list[7][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    delivery_list[7][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    delivery_list[7][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    delivery_list[7][4].append(restaurant)
                if "price" not in restaurant:
                    delivery_list[7][5].append(restaurant)
            if "Salad" in title_list:
                delivery_list[8][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    delivery_list[8][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    delivery_list[8][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    delivery_list[8][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    delivery_list[8][4].append(restaurant)
                if "price" not in restaurant:
                    delivery_list[8][5].append(restaurant)
            if "Chinese" in title_list:
                delivery_list[9][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    delivery_list[9][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    delivery_list[9][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    delivery_list[9][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    delivery_list[9][4].append(restaurant)
                if "price" not in restaurant:
                    delivery_list[9][5].append(restaurant)
            if "Bakeries" in title_list:
                delivery_list[10][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    delivery_list[10][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    delivery_list[10][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    delivery_list[10][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    delivery_list[10][4].append(restaurant)
                if "price" not in restaurant:
                    delivery_list[10][5].append(restaurant)
            if "Sanwitches" not in title_list and "Pizza" not in title_list and "Burgers" not in title_list and "Parks" not in title_list and "Mexican" not in title_list and "Desserts" not in title_list and "Bars" not in title_list and "Salad" not in title_list and "Chinese" not in title_list and "Bakeries" not in title_list:
                delivery_list[11][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    delivery_list[11][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    delivery_list[11][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    delivery_list[11][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    delivery_list[11][4].append(restaurant)
                if "price" not in restaurant:
                    delivery_list[11][5].append(restaurant)

        if "transactions" in restaurant and "pickup" not in restaurant["transactions"] and "delivery" not in restaurant["transactions"]:
            other_list[0].append(restaurant)
            for style in restaurant["categories"]:
                title_list.append(style["title"])
            if "Sanwitches" in title_list:
                other_list[1][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    other_list[1][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    other_list[1][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    other_list[1][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    other_list[1][4].append(restaurant)
                if "price" not in restaurant:
                    other_list[1][5].append(restaurant)
            if "Pizza" in title_list:
                other_list[2][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    other_list[2][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    other_list[2][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    other_list[2][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    other_list[2][4].append(restaurant)
                if "price" not in restaurant:
                    other_list[2][5].append(restaurant)
            if "Burgers" in title_list:
                other_list[3][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    other_list[3][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    other_list[3][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    other_list[3][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    other_list[3][4].append(restaurant)
                if "price" not in restaurant:
                    other_list[3][5].append(restaurant)
            if "Parks" in title_list:
                other_list[4][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    other_list[4][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    other_list[4][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    other_list[4][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    other_list[4][4].append(restaurant)
                if "price" not in restaurant:
                    other_list[4][5].append(restaurant)
            if "Mexican" in title_list:
                other_list[5][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    other_list[5][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    other_list[5][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    other_list[5][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    other_list[5][4].append(restaurant)
                if "price" not in restaurant:
                    other_list[5][5].append(restaurant)
            if "Desserts" in title_list:
                other_list[6][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    other_list[6][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    other_list[6][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    other_list[6][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    other_list[6][4].append(restaurant)
                if "price" not in restaurant:
                    other_list[6][5].append(restaurant)
            if "Bars" in title_list:
                other_list[7][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    other_list[7][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    other_list[7][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    other_list[7][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    other_list[7][4].append(restaurant)
                if "price" not in restaurant:
                    other_list[7][5].append(restaurant)
            if "Salad" in title_list:
                other_list[8][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    other_list[8][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    other_list[8][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    other_list[8][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    other_list[8][4].append(restaurant)
                if "price" not in restaurant:
                    other_list[8][5].append(restaurant)
            if "Chinese" in title_list:
                other_list[9][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    other_list[9][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    other_list[9][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    other_list[9][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    other_list[9][4].append(restaurant)
                if "price" not in restaurant:
                    other_list[9][5].append(restaurant)
            if "Bakeries" in title_list:
                other_list[10][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    other_list[10][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    other_list[10][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    other_list[10][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    other_list[10][4].append(restaurant)
                if "price" not in restaurant:
                    other_list[10][5].append(restaurant)
            if "Sanwitches" not in title_list and "Pizza" not in title_list and "Burgers" not in title_list and "Parks" not in title_list and "Mexican" not in title_list and "Desserts" not in title_list and "Bars" not in title_list and "Salad" not in title_list and "Chinese" not in title_list and "Bakeries" not in title_list:
                other_list[11][0].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$":
                    other_list[11][1].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$":
                    other_list[11][2].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$":
                    other_list[11][3].append(restaurant)
                if "price" in restaurant and restaurant["price"] == "$$$$":
                    other_list[11][4].append(restaurant)
                if "price" not in restaurant:
                    other_list[11][5].append(restaurant)
##########################################################################################################################
##########################################################################################################################
with open("Yelp_Organized.json", "w") as outfile:
    json.dump(List1, outfile)
