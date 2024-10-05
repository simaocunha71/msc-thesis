
    def sort_array(array):
        if not array or len(array) == 1:
            return array
        else:
            sorted_array = sorted(array)
            if (array[0] + array[-1]) % 2 == 0:
                return sorted_array[::-1]
            else:
                return sorted_array

print(sort_array([]))  # []
print(sort_array([5]))  # [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  # [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # [6, 5, 4, 3, 2, 1, 0]

# This solution works by first checking if the array is empty or has only one element. If it is, it simply returns the array as it is. If it has more elements, it sorts the array and then checks if the sum of the first and last elements is even. If it is, it reverses the sorted array. If it is not, it returns the sorted array as is.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
