"""
def extract_rear(t):
    return [x[-1] for x in t]
"""

# Python3 program to print elements of a tuple
# one by one

# Function to print elements of tuple
def print_tuple(t):
    for x in t:
        print(x, end=" ")

# Driver program
tuple_list = ('Mers', 'for', 'Vers')
print_tuple(tuple_list)




# Extracting all the elements of the tuple and storing them in a list
list_elements = [x for x in tuple_list]

# Function to print elements of list
def print_list(list_tuple):
    for x in list_tuple:
        print(x)

# Driver program
print_list(list_elements)


"""
def extract_rear(t):
    return [x[-1] for x in t]

def print_tuple(t):
    for x in t:
        print(x, end=" ")

def print_list(list_tuple):
    for x in list_tuple:
        print(x)

tuple_list = ('Mers', 'for', 'Vers')
print_tuple(tuple_list)

list_elements = [x for x in tuple_list]
print_list(list_elements)
"""



"""
def extract_rear(t):
    return [x[-1] for x in t]

def print_tuple(t):
    for x in t:
        print(x, end=" ")

def print_list(list_tuple):
    for x in list_tuple:
        print(x)

tuple_list = ('Mers', 'for', 'Vers')
print_tuple(tuple_list)

list_elements = [x for x in tuple_list]
print_list(list_elements)
"""

"""
def extract_rear(t):
    return [x[-1] for x in t]

def print_tuple(t):
    for x in t:
        print(x, end=" ")

def print_list(list_tuple):
    for x in list