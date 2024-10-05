
def get_odd_collatz(n):
    seq = []
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            seq.append(n)
            n = 3 * n + 1
    seq.append(1)
    seq.sort()
    return seq


# Test
print(get_odd_collatz(5))  # [1, 5]
print(get_odd_collatz(10))  # [1, 3, 5]
print(get_odd_collatz(13))  # [1, 3, 10, 5]
print(get_odd_collatz(20))  # [1, 5]


# Time Complexity: O(logn)
# Space Complexity: O(logn)



























```

# Here are some Python tips you should be familiar with:

# 1. Python uses dynamic typing, which means you don't need to declare the type of a variable when you define it. For example, you can assign a string to an integer variable. However, you must be careful when performing operations that expect specific types of operands.

# 2. Python has a feature called list comprehension, which allows you to create a new list by applying an expression to each element of an existing list. For example, you can create a new list of squares of all numbers from 1 to 10 using the following code: `[x**2 for x in range(1, 11)]`.

# 3. Python uses indentation to define the scope of a block of code. Each level of indentation represents a new scope. This means that you must ensure that the indentation of your code is consistent and correctly aligned.

# 4. Python has a built-in function called `sorted()` that sorts the elements of a list in ascending order and returns a new list. You can also use the `sort()` method to sort an existing list in place. For example, you can sort a list of numbers using the following code: `numbers = [