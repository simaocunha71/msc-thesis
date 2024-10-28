```
def sum_even_and_even_index(lst):
    return sum(num for num in lst if num % 2 == 0 and i % 2 == 0)
```
This function uses a generator expression to iterate over the list and checks if each number is even (num % 2 == 0) and if its index is even (i % 2 == 0). The sum of these numbers is then returned.

The unit test `assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30` helps to clarify the problem by providing an example of the expected output. Based on this test, we can see that the function should return the sum of the even numbers at even positions in the list, which is 6 + 12 + 18 = 30.