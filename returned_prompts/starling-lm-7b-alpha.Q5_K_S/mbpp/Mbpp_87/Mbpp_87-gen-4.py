def merge_dictionaries_three(d1,d2,d3):
    merged_dict = d1.copy()
    merged_dict.update(d2)
    merged_dict.update(d3)
    return merged_dict

# test
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}



# Python3 program to merge
# two dictionaries

def merge_dict(dict1,
               dict2):

    # Merge by update()
    dict1.update(dict2)

    # Return merged dictionary
    return dict1


# Driver Code
dict1 = {1: "Geeks",
         2: "forGeeks"}

dict2 = {3: "is",
         4: "best"}

print(merge_dict(dict1, dict2))

# This code is contributed
# by Anant Agarwal.



# Python3 program to merge
# three dictionaries

def merge_dict(dict1,
               dict2,
               dict3):

    # Merge by update()
    dict1.update(dict2)
    dict1.update(dict3)

    # Return merged dictionary
    return dict1


# Driver Code
dict1 = {1: "Geeks",
         2: "forGeeks"}

dict2 = {3: "is",
         4: "best"}

dict3 = {5: "platform",
         6: "only"}

print(merge_dict(dict1, dict2, dict3))

# This code is contributed
# by Anant Agarwal.



"""
A function to merge dictionaries
"""
def merge_dict(d1,d2):
    for key in d2:
        if key in d