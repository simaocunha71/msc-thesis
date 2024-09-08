
def is_Monotonic(arr):
    return (all(arr[i] <= arr[i+1] for i in range(len(arr)-1))) or (all(arr[i] >= arr[i+1] for i in range(len(arr)-1)))

print(is_Monotonic([6, 5, 4, 4]))

"""
This function works by checking if all elements in the array are in ascending order (all(arr[i] <= arr[i+1] for i in range(len(arr)-1))) or all elements in the array are in descending order (all(arr[i] >= arr[i+1] for i in range(len(arr)-1))). If either of these conditions is true, the function returns True, indicating that the array is monotonic.

For example, let's take the array [6, 5, 4, 4].
- The first condition (all(arr[i] <= arr[i+1] for i in range(len(arr)-1))) would be True because all elements in the array are in ascending order.
- The second condition (all(arr[i] >= arr[i+1] for i in range(len(arr)-1))) would also be True because all elements in the array are in descending order.

So, both conditions are True, and the function returns True, indicating that the array [6, 5, 4, 4] is monotonic.
"""
<jupyter_output>
True
<jupyter_text>
2. Python program to print all the numbers between two given numbers (inclusive) using while loop.
<jupyter_code>
# Python program to print all the numbers between two given numbers (inclusive) using while loop.

def print_numbers(start, end):
    while start <= end:
        print(start)
        start += 1

print_numbers(1, 10)
<jupyter_output>
1
2
3
4
5
6
7
8
9
10
<jupyter_text>
3. Python program to find the sum of digits of a given number using while loop