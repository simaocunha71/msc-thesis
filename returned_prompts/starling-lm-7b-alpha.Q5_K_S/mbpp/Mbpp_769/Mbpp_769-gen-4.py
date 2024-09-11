"""
def Diff(list_one, list_two):
    result = []
    for i in list_one:
        if i not in list_two:
            result.append(i)
    return result
"""

def Diff(list_one, list_two):
    result = [i for i in list_one if i not in list_two]
    return result

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))
print(Diff([1, 1, 2, 3, 5, 8, 9, 10], [2, 4, 6, 8, 10]))
print(Diff([1, 2, 3, 4, 5, 6], [2, 4, 6, 8]))

"""
The Diff function is defined to accept two lists as arguments. The function then creates an empty list called "result" to store the items that are not in the second list. The function then iterates over each item in the first list using a for loop. For each item, it checks if the item is not in the second list using the "not in" operator. If the item is not in the second list, it appends the item to the "result" list. Finally, the function returns the "result" list.
"""

"""
In the provided code, the Diff function is defined using list comprehension, which is a more concise and efficient way to create a list based on an existing list. The list comprehension syntax "result = [i for i in list_one if i not in list_two]" creates a new list called "result" that contains all the items from "list_one" that are not in "list_two". The "if" statement inside the list comprehension checks if each item from "list_one" is not in "list_two". If the condition is true, the item is added to the "result" list. Finally, the "result" list is returned by the function.
"""

"""
The provided code includes three assert statements to test the Diff function. Each assert statement checks if the output of the Diff function matches the expected output. If the