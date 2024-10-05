
    lst.sort()
    sorted_lst = []
    while lst:
        sorted_lst.append(lst.pop(0))
        if lst:
            sorted_lst.append(lst.pop(-1))
    return sorted_lst

print(strange_sort_list([1, 2, 3, 4]))  #  [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  #  [5, 5, 5, 5]
print(strange_sort_list([]))  #  []

# This solution sorts the list and then pops the first and last elements of the list and appends them to a new list,
# repeating this process until the original list is empty.
# The result is a list that alternates between the smallest and largest remaining elements of the original list.
# This is a solution that meets the requirements of the problem.
<jupyter_output>
[1, 4, 2, 3]
[5, 5, 5, 5]
[]
<jupyter_text>
2. Write a function that takes an array of integers and returns the sum of the integers after performing the following operations:* Sort the array in ascending order* Remove the last element from the array* Add the last element to the beginning of the array* Return the sum of the array
<jupyter_code>
def manipulate_array(arr):
    # Sort the array in ascending order
    arr.sort()

    # Remove the last element from the array
    arr = arr[:-1]

    # Add the last element to the beginning of the array
    arr = [arr[-1]] + arr[:-1]

    # Return the sum of the array
    return sum(arr)

print(manipulate_array([5, 3, 1, 4, 2]))  # Output: 11
print(manipulate_array([10, 7, 5, 8, 6]))  # Output: 33
<jupyter_output>
11
