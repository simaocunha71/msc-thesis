
def fizz_buzz(n: int):
    result = 0
    for i in range(n):
        if (i % 11 == 0) or (i % 13 == 0):
            if str(i).count("7") > 0:
                result += 1
    return result


# These "asserts" using only for self-checking and not necessary for auto-grading
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("*** Test Passed.")
    else:
        print("*** Test Failed.")




# Here you can create nice looking test cases using `def` and `if` statements.
# This is optional and up to you.
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3


# At the end of the file, don't forget to run the `test_fizz_buzz` function to check your implementation!
test_fizz_buzz()
































```

```