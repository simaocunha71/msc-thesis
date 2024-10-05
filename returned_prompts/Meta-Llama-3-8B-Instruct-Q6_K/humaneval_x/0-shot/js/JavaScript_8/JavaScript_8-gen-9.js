Here is the solution in Python:
```
def sumProduct(numbers):
    if not numbers:
        return (0, 1)
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
```
Here's an explanation of the code:

1. We first check if the input list `numbers` is empty. If it is, we return a tuple `(0, 1)`, as per the problem statement.
2. We initialize two variables `sum` and `product` to 0 and 1, respectively. These variables will hold the sum and product of all the integers in the list.
3. We iterate through the list using a for loop, and for each integer `num`, we add it to the `sum` variable and multiply it with the `product` variable.
4. Finally, we return a tuple `(sum, product)`.

You can test this function with the examples provided in the problem statement:
```
print(sumProduct([]))  # Output: (0, 1)
print(sumProduct([1, 2, 3, 4]))  # Output: (10, 24)
```