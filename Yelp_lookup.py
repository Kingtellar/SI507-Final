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
with open("Yelp_Organized.json") as f:
    List1 = json.load(f)

with open("Yelp_Combined.json") as f:
    data = json.load(f)
################################################################################
def display(list, Index = 1):
    for n in range(len(list)):
        print(str(n+Index) + " " + str(list[n]["name"])+ ": phone " + str(list[n]["display_phone"])+ " address "+ str(list[n]["location"]["display_address"]))

#display(List1[2])

style_list = []
price_list = []

for restaurant in data:
    if 'price' in restaurant:
        price_list.append(restaurant['price']) # $ - $$$$ ($,$$)low price, ($$$,$$$$)High price
    for style in restaurant["categories"]:
        style_list.append(style['title'])
#print(len(price_list))
#print(style_list)

def word_count(list):
    word_count = {}
    for word in list:
        if word.isalpha() and len(word) > 1 and word != '\r\n':
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    return  word_count

counted_style_list = word_count(style_list)
ranked_style_list = []
for i,word in enumerate(sorted(counted_style_list,key=counted_style_list.get,reverse=True)):
        ranked_style_list.append(word)

top10_style_list = ranked_style_list[0:10]
#print(top10_style_list)
#display(List1[2][11][1])
def bubbleSort(List):
    for i in range(len(List)):
        for j in range(0, len(List)-i-1):
            if float(List[j]['rating']) < float(List[j+1]['rating']):
                List[j], List[j+1] = List[j+1], List[j]
    return List

if __name__ == "__main__":
    # control code
    while True:
        print()
        user_input = input("Choose an option(number): 1. pickup 2. delivery 3. others, or \"exit\" to quit: ")
        while True:
             if user_input == 'exit':
                 print()
                 print("Bye!")
                 quit()
             elif user_input != '1' and user_input != '2' and user_input != '3':
                 print()
                 print("Pleaase enter a number between 1-3")
                 continue
             elif user_input == '1':
                 while True:
                     print()
                     user_input1 = input("Choose an option(number): 1. Sandwitches 2. Pizza 3. Burgers 4. Parks 5. Mexicaan 6. Desserts 7. Bars 8. Salad 9. Chinese 10. Bakeries 11. Others, or \"exit\" to quit: ")
                     if user_input1 == 'exit':
                         print()
                         print("Bye!")
                         quit()
                     elif user_input1 != '1' and user_input1 != '2' and user_input1 != '3'and user_input1 != '4'and user_input1 != '5'and user_input1 != '6'and user_input1 != '7'and user_input1 != '8'and user_input1 != '9'and user_input1 != '10'and user_input1 != '11':
                         print()
                         print("Pleaase enter a number between 1-11")
                         continue
                     else:
                         while True:
                             print()
                             user_input2 = input("Choose a price level(number): 1. $ 2. $$ 3. $$$ 4. $$$$ 5. Others, or \"back\" to go back, or \"exit\" to quit: ")
                             if user_input2 == 'exit':
                                 print()
                                 print("Bye!")
                                 quit()
                             elif user_input2 == 'back':
                                 break
                             elif user_input2 != '1' and user_input2 != '2' and user_input2 != '3'and user_input2 != '4'and user_input2 != '5':
                                 print()
                                 print("Please enter a number between 1-5")
                                 continue

                             else:
                                 list = []
                                 list = bubbleSort(List1[0][int(user_input1)][int(user_input2)])
                                 if len(list) == 0:
                                     print()
                                     print("No recommendation based on your preference.")
                                     continue
                                 elif len(list) <= 10:
                                     print()
                                     display(list)
                                     while True:
                                         print()
                                         user_input3 = input("Choose the restaurant you are interested in (number), or \"back\" to go back, or \"exit\" to quit: ")
                                         if user_input3 == 'exit':
                                             print()
                                             print("Bye!")
                                             quit()
                                         elif user_input3 == 'back':
                                             break
                                         elif user_input3 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] or int(user_input3) > len(list):
                                             print()
                                             print("Pleaase enter a valid number.")
                                             continue
                                         else:
                                             webbrowser.open(list[int(user_input3)-1]['url'], new=2)
                                             continue

                                 elif len(list) > 10:
                                     print()
                                     display(list[0:10])
                                     while True:
                                         print()
                                         user_input3 = input("Choose the restaurant you are interested in (number), or \"back\" to go back, or \"exit\" to quit: ")
                                         if user_input3 == 'exit':
                                             print()
                                             print("Bye!")
                                             quit()
                                         elif user_input3 == 'back':
                                             break
                                         elif user_input3 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] :
                                             print()
                                             print("Pleaase enter a valid number.")
                                             continue
                                         else:
                                             webbrowser.open(list[int(user_input3)-1]['url'], new=2)
                                             continue



             elif user_input == '2':
                 while True:
                     print()
                     user_input1 = input("Choose an option(number): 1. Sandwitches 2. Pizza 3. Burgers 4. Parks 5. Mexicaan 6. Desserts 7. Bars 8. Salad 9. Chinese 10. Bakeries 11. Others, or \"exit\" to quit: ")
                     if user_input1 == 'exit':
                         print()
                         print("Bye!")
                         quit()
                     elif user_input1 != '1' and user_input1 != '2' and user_input1 != '3'and user_input1 != '4'and user_input1 != '5'and user_input1 != '6'and user_input1 != '7'and user_input1 != '8'and user_input1 != '9'and user_input1 != '10'and user_input1 != '11':
                         print()
                         print("Pleaase enter a number between 1-11")
                         continue
                     else:
                         while True:
                             print()
                             user_input2 = input("Choose a price level(number): 1. $ 2. $$ 3. $$$ 4. $$$$ 5. Others, or \"back\" to go back, or \"exit\" to quit: ")
                             if user_input2 == 'exit':
                                 print()
                                 print("Bye!")
                                 quit()
                             elif user_input2 == 'back':
                                 break
                             elif user_input2 != '1' and user_input2 != '2' and user_input2 != '3'and user_input2 != '4'and user_input2 != '5':
                                 print()
                                 print("Please enter a number between 1-5")
                                 continue

                             else:
                                 list = []
                                 list = bubbleSort(List1[1][int(user_input1)][int(user_input2)])
                                 if len(list) == 0:
                                     print()
                                     print("No recommendation based on your preference.")
                                     continue
                                 elif len(list) <= 10:
                                     print()
                                     display(list)
                                     while True:
                                         print()
                                         user_input3 = input("Choose the restaurant you are interested in (number), or \"back\" to go back, or \"exit\" to quit: ")
                                         if user_input3 == 'exit':
                                             print()
                                             print("Bye!")
                                             quit()
                                         elif user_input3 == 'back':
                                             break
                                         elif user_input3 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] or int(user_input3) > len(list):
                                             print()
                                             print("Pleaase enter a valid number.")
                                             continue
                                         else:
                                             webbrowser.open(list[int(user_input3)-1]['url'], new=2)
                                             continue

                                 elif len(list) > 10:
                                     print()
                                     display(list[0:10])
                                     while True:
                                         print()
                                         user_input3 = input("Choose the restaurant you are interested in (number), or \"back\" to go back, or \"exit\" to quit: ")
                                         if user_input3 == 'exit':
                                             print()
                                             print("Bye!")
                                             quit()
                                         elif user_input3 == 'back':
                                             break
                                         elif user_input3 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] :
                                             print()
                                             print("Pleaase enter a valid number.")
                                             continue
                                         else:
                                             webbrowser.open(list[int(user_input3)-1]['url'], new=2)
                                             continue







             elif user_input == '3':
                 while True:
                     print()
                     user_input1 = input("Choose an option(number): 1. Sandwitches 2. Pizza 3. Burgers 4. Parks 5. Mexicaan 6. Desserts 7. Bars 8. Salad 9. Chinese 10. Bakeries 11. Others, or \"exit\" to quit: ")
                     if user_input1 == 'exit':
                         print()
                         print("Bye!")
                         quit()
                     elif user_input1 != '1' and user_input1 != '2' and user_input1 != '3'and user_input1 != '4'and user_input1 != '5'and user_input1 != '6'and user_input1 != '7'and user_input1 != '8'and user_input1 != '9'and user_input1 != '10'and user_input1 != '11':
                         print()
                         print("Pleaase enter a number between 1-11")
                         continue
                     else:
                         while True:
                             print()
                             user_input2 = input("Choose a price level(number): 1. $ 2. $$ 3. $$$ 4. $$$$ 5. Others, or \"back\" to go back, or \"exit\" to quit: ")
                             if user_input2 == 'exit':
                                 print()
                                 print("Bye!")
                                 quit()
                             elif user_input2 == 'back':
                                 break
                             elif user_input2 != '1' and user_input2 != '2' and user_input2 != '3'and user_input2 != '4'and user_input2 != '5':
                                 print()
                                 print("Please enter a number between 1-5")
                                 continue

                             else:
                                 list = []
                                 list = bubbleSort(List1[2][int(user_input1)][int(user_input2)])
                                 if len(list) == 0:
                                     print()
                                     print("No recommendation based on your preference.")
                                     continue
                                 elif len(list) <= 10:
                                     print()
                                     display(list)
                                     while True:
                                         print()
                                         user_input3 = input("Choose the restaurant you are interested in (number), or \"back\" to go back, or \"exit\" to quit: ")
                                         if user_input3 == 'exit':
                                             print()
                                             print("Bye!")
                                             quit()
                                         elif user_input3 == 'back':
                                             break
                                         elif user_input3 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] or int(user_input3) > len(list):
                                             print()
                                             print("Pleaase enter a valid number.")
                                             continue
                                         else:
                                             webbrowser.open(list[int(user_input3)-1]['url'], new=2)
                                             continue

                                 elif len(list) > 10:
                                     print()
                                     display(list[0:10])
                                     while True:
                                         print()
                                         user_input3 = input("Choose the restaurant you are interested in (number), or \"back\" to go back, or \"exit\" to quit: ")
                                         if user_input3 == 'exit':
                                             print()
                                             print("Bye!")
                                             quit()
                                         elif user_input3 == 'back':
                                             break
                                         elif user_input3 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] :
                                             print()
                                             print("Pleaase enter a valid number.")
                                             continue
                                         else:
                                             webbrowser.open(list[int(user_input3)-1]['url'], new=2)
                                             continue
