
    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop(-1))
    return result


# Test cases
print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(strange_sort_list([]))  # []


"""
The function `strange_sort_list(lst)` sorts the list in a strange order where it firstly takes the smallest number in the list and then the largest number.
This process is repeated until all numbers are used up.

The function uses a while loop to iterate through the list.
At each iteration, it pops the first and last elements from the list and appends them to the result list.
The while loop continues until all elements in the list have been popped and appended to the result list.

Finally, the function returns the result list.
"""
<jupyter_output>
[1, 4, 2, 3]
[5, 5, 5, 5]
[]
<jupyter_text>
3. Write a function that returns the sum of all elements in a list after multiplying each element by its index.
<jupyter_code>
