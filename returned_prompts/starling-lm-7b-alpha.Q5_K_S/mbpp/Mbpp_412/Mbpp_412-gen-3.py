def remove_odd(nums):
    return [num for num in nums if num % 2 == 0]

print(remove_odd([1,2,3]))













"""
As per question,
We need to remove odd numbers from a given list.
So,
We can use List comprehension to create a new list from given list by checking each element with % operator to check if it's odd or even.
And return that new list.

Here is the step by step explanation of code:

We define a function remove_odd that takes a list nums as an argument.
Inside the function we use List comprehension to create a new list.
For each number in the given list nums, if the number is even (i.e., the number % 2 gives 0), we include it in the new list.
Finally, we return the new list.

As per the assert statement, if we pass the list [1,2,3] to the remove_odd function, it should return [2] because 2 is the only even number in the given list.
"""
"""
As per question,
We need to remove odd numbers from a given list.
So,
We can use List comprehension to create a new list from given list by checking each element with % operator to check if it's odd or even.
And return that new list.

Here is the step by step explanation of code:

We define a function remove_odd that takes a list nums as an argument.
Inside the function we use List comprehension to create a new list.
For each number in the given list nums, if the number is odd (i.e., the number % 2 gives 1), we include it in the new list.
Finally, we return the new list.

As per the assert statement, if we pass the list [1,2,3] to the remove_odd function, it should return [1,3] because 1 and 3 are the only odd numbers in the given list.
"""


"""
As per question,
We need to remove odd numbers from a given list.
So,
We can use List comprehension to create a new list from given list by checking each element with %