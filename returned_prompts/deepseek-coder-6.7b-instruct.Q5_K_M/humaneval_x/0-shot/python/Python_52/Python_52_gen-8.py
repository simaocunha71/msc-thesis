
    for i in l:
        if i >= t:
            return False
    return True


print(below_threshold([1, 2, 4, 10], 100))
print(below_threshold([1, 20, 4, 10], 5))


def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    return all(i < t for i in l)


print(below_threshold([1, 2, 4, 10], 100))
print(below_threshold([1, 20, 4, 10], 5))

# Alternatively, you can use a list comprehension and the `any` function:

def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    return not any(i >= t for i in l)


print(below_threshold([1, 2, 4, 10], 100))
print(below_threshold([1, 20, 4, 10], 5))
<jupyter_output>
True
False
True
False
True
False
<jupyter_text>
6. Write a function that takes in a string and returns a dictionary where the keys are the words in the string and the values are the counts of those words.
<jupyter_code>
def word_count(s: str) -> dict:
    """Return a dictionary where the keys are