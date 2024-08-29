
def is_Monotonic(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

print(is_Monotonic([6, 5, 4, 4]))

# Output: True
<jupyter_output>
True
<jupyter_text>
2. Write a Python function to find the largest and smallest number from a list of unsorted integers.
<jupyter_code>
