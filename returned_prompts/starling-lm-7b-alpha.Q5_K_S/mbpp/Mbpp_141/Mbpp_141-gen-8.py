"""
Here's a function that sorts a list in ascending order:

def pancake_sort(lst):
    for i in range(len(lst) // 2):
        max_idx = lst.index(max(lst[:len(lst) - i - 1]))
        lst.pop(max_idx)
        lst.insert(0, max(lst[:len(lst) - i - 1]))
    return lst
"""

This function, `pancake_sort`, takes in a list, `lst`, and sorts it in ascending order. It does so by repeatedly finding the maximum element in the first half of the list and swapping it with the element at the end of the list. This process is repeated until the list is fully sorted.

In the function, we use a `for` loop to iterate over the range of `len(lst) // 2`. This loop ensures that we only consider the first half of the list in each iteration. 

Inside the loop, we find the index of the maximum element in the first half of the list using `max_idx = lst.index(max(lst[:len(lst) - i - 1]))`. We then remove this maximum element from the list using `lst.pop(max_idx)`. 

Next, we insert the maximum element at the beginning of the list using `lst.insert(0, max(lst[:len(lst) - i - 1]))`. This effectively swaps the maximum element with the element at the end of the list. 

After the loop finishes, the list is fully sorted and we return it using `return lst`. 

To test the function, we can use the `assert` statement to ensure that the function correctly sorts the provided list, `[15, 79, 25, 38, 69]`, resulting in the expected output `[15, 25, 38, 69, 79]`.

"""

# Here is a Python3 program to implement Pancake Sort

def pancake_sort(lst):
    for i in range(len(lst) // 2):
        max_idx = lst.index(max(lst[:len(lst) -