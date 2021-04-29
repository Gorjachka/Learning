from tabulate import tabulate

table = [['First Name', 'Last Name', 'Age'], ['John', 'Smith', 39], ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]
table1 = [['First Name', 'Last Name', 'Age'], ['John', 'Smith', 39], ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]
T =tabulate(table, headers='firstrow', tablefmt='fancy_grid')

print(T)

# local_dir = os.path.dirname(__file__)
# with open(("TableFinmon.txt"), "a") as file:  # (os.path.join(local_dir, "TableFinmon.txt"), "w") as file:
#     # for data in listeTableLoc35R:
#     file.write(tabulate())
#     file.close()

