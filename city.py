class City:

    def __init__(self):

        self.name = ""
        self.mayor = ""
        self.yearEstablished = ""
        self.buildings = []

    def add_building(self, new_bldg):

        self.buildings.append(new_bldg)

    def printBuildings(self):

        for bldg in self.buildings:

            date_array = str(bldg.date_constructed).split(" ")
            date = date_array[0]
            split_date = date.split("-")
            final_date = f"{split_date[1]}/{split_date[2]}/{split_date[0]}"
            print(f"{bldg.address} was purchased by {bldg.owner} on {final_date} and has {bldg.stories} stories and is in {self.name} whose mayor is {self.mayor}.")
            print()
