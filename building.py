# Practice: Urban Planner
# Setup
# mkdir -p ~/workspace/python/exercises/planner && cd $_
# touch building.py
# In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city. Create a class named Building in the building.py file and define the following fields, properties, and methods.

# Properties
# designer - It will hold your name.
# date_constructed - This will hold the exact time the building was created.
# owner - This will store the same of the person who owns the building.
# address
# stories
# Methods
# Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

# Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.

# Constructor
# Define your __init__ method to accept two arguments

# address
# stories
# Once defined this way, you can send those values as parameters when you create each instance

#  eight_hundred_eighth = Building("800 8th Street", 12)
# Creating Your Buildings
# Create 5 building instances
# Have each one get purchased by a real estate magnate
# After purchased, construct each one
# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
# Example
# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.

import datetime

class Building:

    def __init__(self, address, stories):

        self.designer = "Trey Suiter"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):

        self.date_constructed = datetime.datetime.now()

    def purchase(self, purchaser):

        self.owner = purchaser


batman_bldg = Building("333 Commerce St", 100)
NSS_bldg = Building("301 Plus Park Blvd", 3)
my_house_bldg = Building("Anderon Ln", 1)
tAndC_ford_bldg = Building("123 Gallatin Rd", 2)
madison_commCenter_bldg = Building("345 DuPont Ave", 4)

batman_bldg.construct()
NSS_bldg.construct()
my_house_bldg.construct()
tAndC_ford_bldg.construct()
madison_commCenter_bldg.construct()

batman_bldg.purchase("Jimmy Jam")
NSS_bldg.purchase("Fred Flippy")
my_house_bldg.purchase("Biance")
tAndC_ford_bldg.purchase("Sam Silly")
madison_commCenter_bldg.purchase("Alan Arf")

all_Bldgs = [batman_bldg, NSS_bldg, my_house_bldg, tAndC_ford_bldg, madison_commCenter_bldg]

# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.

for bldg in all_Bldgs:

    date_array = str(bldg.date_constructed).split(" ")
    date = date_array[0]
    split_date = date.split("-")
    final_date = f"{split_date[1]}/{split_date[2]}/{split_date[0]}"
    print(f"{bldg.address} was purchased by {bldg.owner} on {final_date} and has {bldg.stories} stories.")
    print()