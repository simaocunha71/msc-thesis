

def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
"""


def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
<jupyter_output>
<empty_output>
<jupyter_text>
Task 3: Remove duplicates from a list in Python
<jupyter_code>
"""
