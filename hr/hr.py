# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    table = data_manager.get_table_from_file("hr/persons.csv")
    while True:
        options = ["Print the table records",
                   "Add an item to the table",
                   "Remove from table",
                   "Update an item in the table",
                   "Who is the oldest person?",
                   "Who is the closest to the average age y?"]

        ui.print_menu("Human Resources", options, "Back")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
            data_manager.write_table_to_file("hr/persons.csv", table)
        elif option == "3":
            id_ = ui.get_inputs(["Please enter an ID to remove: "], "")
            remove(table, id_)
            data_manager.write_table_to_file("hr/persons.csv", table)
        elif option == "4":
            id_ = ui.get_inputs(["Please enter an ID to update: "], "")
            update(table, id_)
            data_manager.write_table_to_file("hr/persons.csv", table)
        elif option == "5":
            label = "The oldest person is:"
            result = get_oldest_person(table)
            ui.print_result(result, label)
        elif option == "6":
            label = "Person closest to average age:"
            result = get_persons_closest_to_average(table)
            ui.print_result(result, label)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        return


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "name", "birthdate"]
    ui.print_table(data_manager.get_table_from_file("hr/persons.csv"), title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["name", "birth year"]
    args = []
    args.append(common.generate_random(table))
    for arg in range(len(title_list)):
        args.append(ui.get_inputs(("Please enter the " + title_list[arg]), ""))
        table.append(args)
        return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    name_id = str(id_[1])
    for row in table:
        original_id = row[1]
        if original_id == user_id:
            table.remove(row)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @t    able: list of lists
# @id_: string
def update(table, id_):
    list_labels = ["name", "birthdate"]
    user_id = str(id_[0])
    for row in range(len(table)):
        original_id = table[row][0]
        if original_id == user_id:
            new_data = ui.get_inputs(list_labels, "Update data")
            new_data.insert(0, user_id)
            table[row] = new_data
            return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    min = 2016
    people = []
    names = []
    for year in table:
        if int(year[2]) < min:
            min = int(year[2])
    for name in table:
        if int(name[2]) == min:
            people.append(name[1])
    return people


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    person_closest_average = []
    average = 0
    counter = 0
    for row in table:
        average += int(row[2])
        counter += 1
    average = average / counter
    difference = 9999
    if abs(int(row[2]) - average) < difference:
        difference = abs(int(row[2]) - average)
    for row in table:
        if difference == abs(int(row[2]) - average):
            person_closest_average.append(row[1])
    return person_closest_average
