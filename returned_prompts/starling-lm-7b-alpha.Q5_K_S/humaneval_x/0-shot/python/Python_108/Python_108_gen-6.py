
def count_nums(arr):
    res = 0
    for elem in arr:
        if abs(elem) != elem:
            res += 1
        else:
            res += sum(map(int, str(elem))) > 0
    return res


# These are here to avoid circular import problems
count_nums = count_nums



def test_count_nums():
    assert count_nums([]) == 0
    assert count_nums([-1, 11, -11]) == 1
    assert count_nums([1, 1, 2]) == 3

if __name__ == "__main__":
    test_count_nums()





























```
Here's how this code works:

- The function `count_nums` is defined with a single parameter, `arr`, which is the array of integers that the function is called on.
- The variable `res` is initialized to 0. This variable will keep track of the number of elements in the array that have a sum of digits greater than 0.
- A for loop is used to iterate over each element in the array.
- Inside the for loop, there is an if statement that checks if the absolute value of the element is not equal to the element itself. This condition is true if the element is negative.
- If the element is negative, then the variable `res` is incremented by 1.
- If the element is not negative, then the sum of the digits of the element is calculated using the `sum` function and the `map` function. The `map` function is used to convert each digit in the string representation of the element to an integer, and the `sum` function is used to sum up these integers. If the sum of the digits is greater than 0, then the variable `res` is incremented by 1.
- After the for loop has finished iterating over all the elements in the array, the function returns the value of the variable `res`.
- The test cases at the end of the code are used to verify that the function `count_nums` works