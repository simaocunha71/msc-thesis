def first_odd(lst):
    for i in range(0,len(lst)):
        if lst[i]%2!=0:
            return lst[i]
    return -1

# Testing the function
print(first_odd([1,3,5])) # Returns 1
print(first_odd([2,4,6])) # Returns 2
print(first_odd([10,20,30])) # Returns 10
print(first_odd([1,2,3,4,5])) # Returns 1
print(first_odd([])) # Returns -1




















"""
Correct Solution:

def first_odd(lst):
    for i in range(0,len(lst)):
        if lst[i]%2!=0:
            return lst[i]
    return -1
"""
"""
In the above code, we define a function called `first_odd` that takes a list of numbers as an argument.
We then use a `for` loop to iterate through each element in the list.
Inside the loop, we check if the current element is odd by using the modulo operator `%` to check if the element is not divisible by 2.
If the element is odd, we return the element.
If we reach the end of the loop without finding an odd element, we return -1 to indicate that no odd element was found in the list.

We then test the function by calling it with several different lists of numbers.
For each test case, we print the result of the function call, which should be the first odd number in the list, or -1 if no odd number is found.
"""


"""
The time complexity of this solution is O(n), where n is the length of the input list.
This is because we need to iterate through each element in the list to check if it is odd.
The space complexity is O(1), as we are only using a single variable `i` to keep track of our position in the list.

To optimize this solution, we could use a more efficient algorithm to find the first odd number in the list.
One approach is to use a `while`