def median_numbers(x,y,z):
    arr = [x,y,z]
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2
    else:
        return arr[len(arr)//2]

def test_median_numbers():
    assert median_numbers(25,55,65)==55.0
    print("All tests passed.")

test_median_numbers()












"""
def median_numbers(x,y,z):
    arr = [x,y,z]
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2
    else:
        return arr[len(arr)//2]

def test_median_numbers():
    assert median_numbers(25,55,65)==55.0
    print("All tests passed.")

test_median_numbers()
"""


```
The above code defines a function called `median_numbers` that takes three numbers as input and calculates the median of those numbers. The function first creates a list `arr` containing the three input numbers, sorts the list in ascending order using the `sort()` method, and then calculates the median based on the length of the list. If the length of the list is even (i.e., divisible by 2), the median is calculated as the average of the two middle elements. If the length of the list is odd, the median is simply the middle element.

The code also includes a test function `test_median_numbers()` that calls the `median_numbers` function with the input values (25, 55, 65) and asserts that the result is equal to 55.0. If the assertion passes, the function prints "All tests passed."

To use this code, you can call the `median_num