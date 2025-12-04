# project-10b

# Gabriel Venegas
# GitHub username: GVenegas1
# Date: 12/03/2025

#this lets us work with json files
import json

def search_nobel(year, category):
    """This function looks for Nobel Prize winners by year and category.
    It returns a sorted list of surnames of the winners. """

    #Opens the .json file and read its content
    with open("nobels.json", "r") as file:

        #turn json into Python data (dictionary + lists)
        data = json.load(file)

    #list to store winners' surnames
    surnames = []

    #Go through all the prizes in the data
    for prize in data["prizes"]:

        #Checks if the prize matches the year and category we want
        if prize["year"] == year and prize["category"] == category:

            #Some prizes have multiple winners
            for winner in prize.get("laureates", []):

                #make sure the surname exists
                if "surname" in winner:
                    surnames.append(winner["surname"])

    #Sort the surnames alphabetically and return them
    return sorted(surnames)

 #Example usage
#print(search_nobel("2001","economics"))
