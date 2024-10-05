def string_sequence(n: int) -> str:
    return ' '.join(map(str, range(n+1)))
    # The map function applies the str() function to each number in the range from 0 to n (inclusive)
    # The join() function then concatenates these strings with spaces in between.  # noqa: F401
    # The '+1' is because the range() function in Python is exclusive of the end value, i.e., it stops at n-1.  # noqa: F401
    # So we need to add 1 to n to include n in the sequence.  # noqa: F401
    # For example, range(5) will generate numbers from 0 to 4, but we want to include 5 in the sequence.  # noqa: F401
    # So we use range(n+1) to include n in the sequence.  # noqa: F401
    # The map() function applies the str() function to each number in the range from 0 to n (inclusive)  # noqa: F401
    # and returns a map object, which is then joined() with spaces to create the final string.  # noqa: F401
    # The '+1' is because the range() function in Python is exclusive of the end value, i.e., it stops at n-1.  # noqa: F401
    # So we need to add 1 to n to include n in the sequence.  # noqa: F401
    # For example, range(5) will generate numbers from 0 to 4, but we want to include 5 in the sequence.  # noqa: F401
    # So we use range(n+1) to include n in the sequence.  # noqa: F401
    # The map() function applies the str() function to each number in the range from 0 to n (inclusive)  # noqa: F401
    # and returns a map object, which is then joined() with spaces to create the final string.  # noqa: F401
    # The '+1' is because the range() function in Python is exclusive of the end value, i.e., it stops at n-1.  # noqa: F401
    # So we need to add 1 to n to include n in the sequence.  # noqa: F401
    # For example, range(5) will generate