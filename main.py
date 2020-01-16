# Practice: Urban Planner II
# Setup
# cd ~/workspace/python/exercises/planner
# touch main.py city.py
# In the previous Urban Planner exercise, you practices defining custom types to represent buildings. Now you need to create a type to represent your city. Here are the requirements for the class. You define the properties and methods.

# Name of the city.
# The mayor of the city.
# Year the city was established.
# A collection of all of the buildings in the city.
# A method to add a building to the city.
# Remember, each class should be in its own file. Define the City class in the city.py file.

# Importing into Main
# Open the main.py file and import the Building class from building.py. Once you have defined your City class, also import that into main.py. For this exercise, all the logic of constructing buildings and building your city will be in main.py, so take all of your logic from building.py and move it over to main.

# main.py
# from building import Building
# from city import City
# Birth of a City
# Create a new city instance and add your building instances to it. Once all buildings are in the city, iterate the city's building collection and output the information about each building in the city.

# main.py
# megalopolis = City()

# # Awesome code here

# for building in megalopolis.buildings:
#     print(building)

from building import Building
from city import City

batman_bldg = Building("333 Commerce St", 100)
my_house_bldg = Building("Anderon Ln", 1)
tAndC_ford_bldg = Building("123 Gallatin Rd", 2)
madison_commCenter_bldg = Building("345 DuPont Ave", 4)
nash_soft_school_bldg = Building("301 Plus Park", 5)


batman_bldg.construct()
my_house_bldg.construct()
tAndC_ford_bldg.construct()
madison_commCenter_bldg.construct()
nash_soft_school_bldg.construct()

batman_bldg.purchase("Jimmy Jam")
my_house_bldg.purchase("Biance")
tAndC_ford_bldg.purchase("Sam Silly")
madison_commCenter_bldg.purchase("Alan Arf")
nash_soft_school_bldg.purchase("Some Dude")

all_Bldgs = [nash_soft_school_bldg, batman_bldg, my_house_bldg, tAndC_ford_bldg, madison_commCenter_bldg]

# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.

# for bldg in all_Bldgs:

#     date_array = str(bldg.date_constructed).split(" ")
#     date = date_array[0]
#     split_date = date.split("-")
#     final_date = f"{split_date[1]}/{split_date[2]}/{split_date[0]}"
#     print(f"{bldg.address} was purchased by {bldg.owner} on {final_date} and has {bldg.stories} stories.")
#     print()

megalopolis = City()
megalopolis.name = "Big Ole City"
megalopolis.mayor = "Fancy Pants McMayor Face"
megalopolis.yearEstablished = "2001"

for building_to_add_to_city in all_Bldgs:
    megalopolis.add_building(building_to_add_to_city)

megalopolis.printBuildings()

