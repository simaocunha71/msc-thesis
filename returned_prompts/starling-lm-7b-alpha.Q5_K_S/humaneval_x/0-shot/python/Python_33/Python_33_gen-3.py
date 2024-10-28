
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    thirds = [i for i in l if i % 3 == 0]
    thirds.sort()
    indices = [i for i, x in enumerate(l) if x % 3 == 0]

    for i, x in enumerate(l):
        if i in indices:
            l[i] = thirds[i//3]
    return l


# Created by: Madelyn
# Date: Jan 25, 2021
# This program takes a list and returns the same list with the numbers that are multiples of 3 sorted in order.


# Here are some test cases to check if your code is working. You can add more of your own tests.
# Note that the print statements are just for you to see if the tests are passing or not.

print(sort_third([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Output: [2, 6, 3, 4, 8, 9, 5]

# To check your code, you can use the doctest module.
# In the terminal, navigate to the directory where your python file is saved and run the following command: python -m doctest your_file_name.py

```
 
```

```

```

```

```

```

```
