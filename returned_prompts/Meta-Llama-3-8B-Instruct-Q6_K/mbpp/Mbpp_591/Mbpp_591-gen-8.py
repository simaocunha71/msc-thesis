```
def swap_List(input_list):
    if len(input_list) > 1:
        input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return input_list
```
The problem asks to write a function that swaps the first and last elements in a list. The unit test provided suggests that the list can contain any type of elements, not just integers.

In the solution, I used Python's tuple assignment feature to swap the first and last elements. The `input_list[0], input_list[-1]` syntax is used to assign the value of the last element to the first element, and the value of the first element to the last element. This operation is done only if the list has more than one element, as swapping is not possible with a list containing only one element. The function then returns the modified list. 