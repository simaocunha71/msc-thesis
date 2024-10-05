
    return sorted(set(l))


if __name__ == "__main__":
    import doctest
    doctest.testmod()


This solution uses the built-in `set` function to remove duplicates, and then sorts the resulting list.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2: Return the second largest number in a listThe second largest number in a list is the second largest distinct number. If there are fewer than two distinct numbers in the list, return `None`.
<jupyter_code>
