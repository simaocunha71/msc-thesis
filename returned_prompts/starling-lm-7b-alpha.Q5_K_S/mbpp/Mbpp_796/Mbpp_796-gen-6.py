"""
To solve this, we can use a for loop to iterate over the dictionary items. We can then add up all the values in the dictionary to find the sum.
"""

def return_sum(d):
    sum = 0
    for i in d.values():
        sum += i
    return sum

# Testing
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600


def test_return_sum(d):
    assert return_sum(d) == 600

def test_return_sum_2(d):
    assert return_sum(d) == 500

def test_return_sum_3(d):
    assert return_sum(d) == 400




def main():
    d = {'a': 100, 'b':200, 'c':300}
    print(return_sum(d))

if __name__ == "__main__":
    main()




"""
The above code defines a function called return_sum which takes in a dictionary called d as its parameter. It initialises a variable called sum to 0. Then, using a for loop, it iterates over all the values in the dictionary and adds them up to the sum variable. Finally, it returns the sum.

To test the function, we have written a number of test cases using the assert statement. Each test case asserts that the function returns the expected sum for a given dictionary. If the assertion is true, the test passes; otherwise, it fails.

In the main function, we define a dictionary called d with three key-value pairs. We then call the return_sum function with this dictionary as the argument and print the result.

Overall, this code provides a way to find the sum of all items in a given dictionary using the return_sum function.
"""

# Python Program to find the sum of all items in a given dictionary
# Using a for loop to iterate over the dictionary items

def return_sum(d):
    sum = 0
    for i in d.values():
        sum += i
    return sum

# Testing
assert return