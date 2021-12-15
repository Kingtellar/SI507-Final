# SI507-Final
SI507 Final Project
# How to supply API keys
- Create a yelp app at https://www.yelp.com/fusion to request an API Key.
- Copy the your API Key into the API_KEY in the Yelp_fetch_data.py.

# Required Package
- requests
- webbrowser
- argparse
- pprint
- urllib
- sys

# Data Structure: Tree
```
-pickup_list = [[],
                [[],[],[],[],[],[]],
                [[],[],[],[],[],[]],
                [[],[],[],[],[],[]],
                [[],[],[],[],[],[]],
                [[],[],[],[],[],[]],
                [[],[],[],[],[],[]],
                [[],[],[],[],[],[]],
                [[],[],[],[],[],[]],
                [[],[],[],[],[],[]],
                [[],[],[],[],[],[]],
                [[],[],[],[],[],[]]
               ]
-delivery_list = [[],
                  [[],[],[],[],[],[]],
                  [[],[],[],[],[],[]],
                  [[],[],[],[],[],[]],
                  [[],[],[],[],[],[]],
                  [[],[],[],[],[],[]],
                  [[],[],[],[],[],[]],
                  [[],[],[],[],[],[]],
                  [[],[],[],[],[],[]],
                  [[],[],[],[],[],[]],
                  [[],[],[],[],[],[]],
                  [[],[],[],[],[],[]]
                 ]
-other_list = [[],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]]
              ]
-List1 = [[], [], []]
-List1[0] = pickup_list
-List1[1] = delivery_list
-List1[2] = other_list
```
# Interaction Instructions
- Make sure Yelp_Combined.json and Yelp_Organized.json and Yelp_lookup.py are in your work space.
- Run Yelp_lookup.py in your command window.
- Choose from Pickup, Delivery or Others, this is a one time choice.
- Choose from the top 10 cusine styles or choose others.
- Choose your desired price level, or others for restaurants without specific price level, or go back to rechoose cusine styles.
- A list of recommended restaurant will be printed out in the command window, ranked based on their user ratings from high to low.
- You can choose the restaurant you are insterested in, which will take you to the yelp webpage for that restaurant or go back to remake choices.
- Type exit to exit the program at anytime.
