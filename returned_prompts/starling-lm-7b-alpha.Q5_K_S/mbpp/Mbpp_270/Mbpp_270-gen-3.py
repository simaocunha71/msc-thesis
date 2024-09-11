"""
def sum_even_and_even_index(lst):
    sum = 0
    for i in range(0,len(lst),2):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum

def test_sum_even_and_even_index():
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30

test_sum_even_and_even_index()
"""

def sum_even_and_even_index(lst):
    sum = 0
    for i in range(0,len(lst),2):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum

def test_sum_even_and_even_index():
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30

test_sum_even_and_even_index()



```

In the above solution, the function `sum_even_and_even_index` takes in a list as an argument and initializes a variable `sum` to 0. It then iterates over the indices of the list in even steps using the `range` function with a step size of 2. Inside the loop, it checks if the value at the current index is divisible by 2 (i.e., even). If it is, the value is added to the `sum` variable. Finally, the function returns the sum.

The `test_sum_even_and_even_index` function is used to test the `sum_even_and_even_index` function. It asserts that the function correctly calculates the sum of even numbers at even positions in the given list `[5, 6, 12, 1, 18, 8]`, which should be 30.

When the `test_sum_even_and_even_index` function is called, it executes the assertion and checks if the actual result of the `sum_even_and_even_index`