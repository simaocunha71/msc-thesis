
    return max(l)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# Or you could also use a for loop to iterate through the list and return the maximum element.


def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    max_el = l[0]
    for i in l:
        if i > max_el:
            max_el = i
    return max_el


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# This version of the function uses a for loop to iterate through the list. It starts by setting max_el to the first element of the list. Then it iterates through the list. If it encounters an element that is larger than max_el, it updates max_el to that element. Finally, it returns max_el, which is the maximum element in the list.
<jupyter_output>
<empty_output>
<jupyter_text>
Exercise 2: Write a function that computes the sum of all elements in a list.
<jupyter_code>
# You can use the built-in Python function sum() to compute the sum of all elements in a list.


def sum_elements(l: list):
    """Return the sum of all elements in the list.
    >>> sum_elements([1, 2, 3])
    6
    >>> sum_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    111
    """

    return sum(l)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Alternatively,