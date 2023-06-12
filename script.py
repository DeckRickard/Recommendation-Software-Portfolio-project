from locations import locations

# Initial variable declarations. This should allow the program to be more dynamic.
city = "Istanbul"
categories = [category for category in locations[list(locations.keys())[0]]]

# The welcome message will greet the user, perform initial set up, and pass on to other functions to complete a run of the program.
def welcome():
    print(f"Welcome to the City guide for {city}. You can search here for recommendations based on a number of categories: ")
    print("After searching, a filtered list will be displayed that you can then search again to filter your results further.")
    print("We hope you enjoy your time using this software.")
    print("First things first, let's choose a category to search. The available categories are: ")
    print_data(categories)
    category = choose_category(categories)

def autocomplete():
    pass

def search():
    pass

# Helper function to list the choices that are available to the user in a certain category.
def print_data(data_type):
    for i in range(0, len(data_type)):
        print(f"{i + 1}: {data_type[i]}") 

def choose_category(category_list):
    choice = int(input("Please choose a category by inputting the number associated with it: "))
    if choice > len(category_list) or choice < 0:
        print(f"Invalid choice. Please enter a number between 1 and {len(category_list)}.")
        choose_category(category_list)
    else:
        print("You have chosen: " + category_list[choice - 1])
        return category_list[choice - 1]

welcome()

