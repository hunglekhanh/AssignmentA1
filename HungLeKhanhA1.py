# 

from operator import itemgetter
import sys
import csv


print("Shopping List 1.0 - by Le Khanh Hung\n3 items loaded from items.csv")


def get_menu():
    choice = input("Menu:\nR - List required items\nC - List completed items\n"
                   "A - Add new items\nM - Mark an item as completed\nQ - Quit\n>>>")
    return choice


def load_item():
    import os

    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in '%s': %s" % (cwd, files))
    with open('/Users/PaP/PycharmProjects/Assignment1/item.csv') as item_file:
        reader = csv.reader(item_file)
        item_data = reader.readlines()
        reader.close()
    new_item_data = []
    for a in item_data:
        split_data = a.strip().split(", ")
        new_item_data.append(split_data)
        new_item_data.sort(key=itemgetter(2))
    print(new_item_data)
    required_item_name = []
    required_item_price = []
    required_item_priority = []
    completed_item_name = []
    completed_item_price = []
    completed_item_priority = []
    for a in new_item_data:
        if a[3] == "r":
            required_item_name.append(a[0])
            required_item_price.append(a[1])
            required_item_priority.append(a[2])
        else:
            completed_item_name.append(a[0])
            completed_item_price.append(a[1])
            completed_item_priority.append(a[2])
    return required_item_name, required_item_price, required_item_priority, completed_item_name, \
        completed_item_price, completed_item_priority


def list_required_items():
    required_item_name, required_item_price, required_item_priority, completed_item_name, \
        completed_item_price, completed_item_priority = load_item()
    total_required_price = [float(price) for price in required_item_price]
    print(required_item_price)
    if len(required_item_name) == 0:
        print("No required items")
    else:
        for a in range(len(required_item_name)):
            print("{}. $ {} $ {} ({})".format(a, required_item_name[a],
                                              required_item_price[a], required_item_priority[a]))
        print("Total expected price for {} items: ${}".format(len(required_item_name), sum(total_required_price)))


def list_completed_items():
    required_item_name, required_item_price, required_item_priority, completed_item_name, \
        completed_item_price, completed_item_priority = load_item()
    total_completed_price = [float(price) for price in completed_item_price]
    if len(completed_item_price) == 0:
        print("No completed items")
    else:
        for a in range(len(completed_item_name)):
            print("{}. {} $ {} ({})".format(a, completed_item_name[a],
                                            completed_item_price[a], completed_item_priority[a]))
        print("Total expected price for {} items: ${}".format(len(completed_item_name), sum(total_completed_price)))


def add_new_item():
    item_name = str(input("Item name:"))
    while not item_name.strip():
        print("Input can not be blank")
        item_name = str(input("Item name:"))
    else:
        pass

    item_price_legit = False
    while not item_price_legit:
        try:
            item_price = float(input("Price:"))
            while float(item_price) <= 0:
                print("Price must be >= 0")
                item_price = float(input("Price:"))
            item_price_legit = True
        except ValueError:
            print("Invalid input; enter a valid number")

    item_priority_legit = False
    while not item_priority_legit:
        try:
            item_priority = int(input("Priority:"))
            while item_priority not in range(1, 4):
                print("Priority must be 1, 2 or 3")
                item_priority = int(input("Priority:"))
            item_priority_legit = True
        except ValueError:
                print("Invalid input; enter a valid number")

    print("{}, ${} (priority {}) added to shopping list".format(item_name, item_price, item_priority))
    PRODUCT_FILE = open("item.csv", "a")
    PRODUCT_FILE.write("{},{},{},r\n".format(item_name, item_price, item_priority))
    PRODUCT_FILE.close()


def mark_completed_item():
    required_item_name, required_item_price, required_item_priority, completed_item_name, \
        completed_item_price, completed_item_priority = load_item()
    total_required_price = [float(price) for price in required_item_price]
    if len(required_item_name) != 0:
        for a in range(len(required_item_name)):
            print("{}. $ {} $ {} ({})".format(a, required_item_name[a],
                                              required_item_price[a], required_item_priority[a]))
        print("Total expected price for {} items: ${}".format(len(required_item_name), sum(total_required_price)))
        mark_item_legit = False
        while not mark_item_legit:
            try:
                mark_item = int(input("Enter the number of an item to mark as completed:"))
                while mark_item >= len(required_item_name):
                    print("Invalid item number")
                    mark_item = int(input("Enter the number of an item to mark as completed:"))
                else:
                    item_file = open("item.csv", "w+")
                    if len(completed_item_name) != 0:
                        for a in range(len(completed_item_name)):
                            item_file.write("{},{},{},c\n".format(completed_item_name[a], completed_item_price[a],
                                                                  completed_item_priority[a]))
                    else:
                        pass
                    for a in range(len(required_item_name)):
                        if a == mark_item:
                            item_file.write("{},{},{},c\n".format(required_item_name[a], required_item_price[a],
                                                                  required_item_priority[a]))
                        elif a != mark_item:
                            item_file.write("{},{},{},r\n".format(required_item_name[a], required_item_price[a],
                                                                  required_item_priority[a]))
                    item_file.close()
                mark_item_legit = True
            except ValueError:
                print("Invalid input; enter a valid number")
    else:
        print("No required items")


def main():
    while True:
        try:
            user_choice = get_menu()
            while user_choice != "R" and user_choice != "r" and user_choice != "C" and user_choice != "c" \
                    and user_choice != "A" and user_choice != "a" and user_choice != "M" and user_choice != "m" \
                    and user_choice != "Q" and user_choice != "q":
                print("Invalid menu choice")
                user_choice = get_menu()
            if user_choice == "R" or user_choice == "r":
                list_required_items()
            elif user_choice == "C" or user_choice == "c":
                list_completed_items()
            elif user_choice == "A" or user_choice == "a":
                add_new_item()
            elif user_choice == "M" or user_choice == "m":
                mark_completed_item()
            else:
                print("Items saved to item.csv\nHave a nice day : )")
                sys.exit()
        except ValueError:
            print("Invalid menu choice")


main()
