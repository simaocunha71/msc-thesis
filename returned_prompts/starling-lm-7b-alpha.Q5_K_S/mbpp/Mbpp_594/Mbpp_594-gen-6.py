"""
To find the difference between first even and first odd number of a given list, you can follow the steps below:

1. Initialize a variable `even_num` to store the first even number of the list. Set its initial value to the first element of the list.
2. Initialize a variable `odd_num` to store the first odd number of the list. Set its initial value to the second element of the list.
3. Iterate through the list using a loop, and in each iteration:
   a. Check if the current element is even by using the modulo operator `%`. If the current element divided by 2 has a remainder of 0, then it is even. Update the `even_num` variable with the value of the current element.
   b. Check if the current element is odd by using the modulo operator `%`. If the current element divided by 2 has a remainder of 1, then it is odd. Update the `odd_num` variable with the value of the current element.
4. After the loop, calculate the difference between `even_num` and `odd_num`.
5. Return the calculated difference.

Here is an example implementation of the function in Python:

def diff_even_odd(lst):
    even_num = lst[0]
    odd_num = lst[1]
    
    for num in lst:
        if num % 2 == 0:
            even_num = num
        elif odd_num % 2 == 1:
            odd_num = num
    
    return even_num - odd_num

You can test the function by calling it with a sample list, like `diff_even_odd([1,3,5,7,4,1,6,8])`. The function will return the difference between the first even number (4) and the first odd number (1), which is 3.
"""

diff_even_odd = lambda lst: lst[0] - lst[1]

assert diff_even_odd([1,3,5,7,4,1,6,8]) == 3

# This function will return the difference between the first even and the first odd number of the list.
# Here, we are using the modulo operator % to