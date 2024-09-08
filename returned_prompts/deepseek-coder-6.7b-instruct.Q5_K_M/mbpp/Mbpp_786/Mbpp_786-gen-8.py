def right_insertion(lst, num):
    for i in range(len(lst)):
        if lst[i] > num:
            return i
    return len(lst)

print(right_insertion([1,2,4,5],6))

"""
The function right_insertion takes a sorted list and a number as arguments. 
It iterates over the list. If a number in the list is larger than the given number, it returns the index of that number.
If the function doesn't find such a number, it returns the length of the list, meaning that the number should be appended at the end of the list.
"""

# another way using built-in function
def right_insertion(lst, num):
    return len([i for i in lst if i <= num])

print(right_insertion([1,2,4,5],6))

"""
This function does the same thing as the previous one, but it uses a list comprehension to create a new list that includes only the numbers that are less than or equal to the given number.
It then returns the length of this new list, which is the index of the right insertion point for the given number in the sorted list.
"""
<jupyter_output>
4
4
<jupyter_text>
