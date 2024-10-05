# Here's a step-by-step explanation of the solution:

First, define the function will_it_fly that takes two parameters, q and w.

Next, check if q is a palindromic list. A list is palindromic if it's the same forwards and backwards. You can use the slicing technique to check this. For example, if q is [1, 2, 3], then q[::-1] is [3, 2, 1], which means q is a palindromic list. If q is not a palindromic list, return False.

If q is a palindromic list, calculate the sum of its elements by using the built-in sum() function. For example, if q is [1, 2, 3], then sum(q) is 6.

Check if the sum of q's elements is less than or equal to the maximum possible weight w. If it is, return True. Otherwise, return False.

Here's the code for the solution:

```python
def will_it_fly(q, w):
    # Check if q is a palindromic list
    if q != q[::-1]:
        return False
    # Calculate the sum of q's elements
    total = sum(q)
    # Check if the sum is less than or equal to the maximum possible weight
    if total <= w:
        return True
    else:
        return False
```

You can use this function to determine if an object will fly based on its weight and balance.

Let's try some examples:

```python
print(will_it_fly([1, 2], 5))  # False
print(will_it_fly([3, 2, 3], 1))  # False
print(will_it_fly([3, 2, 3], 9))  # True
print(will_it_fly([3], 5))  # True
```

The output of these examples matches the given examples in the question.

In summary, the function will_it_fly checks if an object will fly by determining if it is balanced (palindromic) and if the sum of its elements