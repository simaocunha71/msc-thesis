
    def sort_array(array):
        if not array or len(array) == 1:
            return array
        if (array[0] + array[-1]) % 2 == 0:
            return sorted(array, reverse=True)
        return sorted(array)


print(sort_array([]))  # → []
print(sort_array([5]))  # → [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  # → [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # → [6, 5, 4, 3, 2, 1, 0]

# ✔️
<jupyter_output>
[]
[5]
[0, 1, 2, 3, 4, 5]
[6, 5, 4, 3, 2, 1, 0]
<jupyter_text>
Explanation:The function `sort_array` takes an array as its argument. If the array is empty or has only one element, it returns the array itself (since an array of one element is already sorted). If the sum of the first and last elements in the array is even, it returns the array sorted in descending order. If the sum is odd, it returns the array sorted in ascending order.
<jupyter_code>
# 💡
<jupyter_output>
<empty_output>
<jupyter_text>
Note:The `sorted` function in Python returns a new sorted list from the elements of any sequence. The `reverse` parameter, when set to `True`, sorts the list in descending order.
<jupyter_code>
# 📒
<jupyter_output>
<empty_output>
<jupyter_text>
References:Python documentation: - [sorted](https://docs.python.org/3/library/functions.htmlsorted) - [reverse](https