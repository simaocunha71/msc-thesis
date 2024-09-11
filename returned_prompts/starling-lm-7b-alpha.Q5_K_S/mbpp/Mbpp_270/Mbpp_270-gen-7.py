"""
def sum_even_and_even_index(lst):
    sum_even = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 == 0:
            sum_even += lst[i]
    return sum_even


sum_even_and_even_index([5, 6, 12, 1, 18, 8])
"""

def sum_even_and_even_index(lst):
    sum_even = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 == 0:
            sum_even += lst[i]
    return sum_even


sum_even_and_even_index([5, 6, 12, 1, 18, 8]) # 30

# assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30

```
In this function, we're using a for loop to iterate through each element in the list. We check if the element is even (using the modulus operator `%`) and if its index is also even. If both conditions are true, we add the element to the `sum_even` variable. Finally, we return the `sum_even` variable, which will contain the sum of all even numbers at even positions in the list.

To test the function, we call it with the provided list `[5, 6, 12, 1, 18, 8]` and print the result, which should be `30`. 

Additionally, we can use the `assert` keyword to check if the function correctly returns the expected result. If the function does not return `30`, the assertion will fail and an error will be raised.
```