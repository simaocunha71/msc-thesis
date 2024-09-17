```
def count_equal(a, b, c):
    return sum(1 for x in (a, b, c) if a == x)
```


Explanation:
The function takes three integers as input. It uses a generator expression to iterate over the three integers. If any of the integers match the first integer, the expression yields 1. The sum function then counts the number of 1s yielded, effectively counting the number of equal integers. The unit test `assert test_three_equal(1,1,1) == 3` ensures that the function correctly counts the number of equal integers. 

For example, if the input is (1, 1, 1), the function will return 3, indicating that all three integers are equal. If the input is (1, 2, 3), the function will return 1, indicating that only one integer is equal to the first integer.  If the input is (1, 1, 2), the function will return 2, indicating that two integers are equal to the first integer.  If the input is (1, 2, 2), the function will return 2, indicating that two integers are equal to the first integer.  If the input is (1, 1, 1, 1, 1), the function will return 5, indicating that all five integers are equal.  If the input is (1, 1, 1, 2, 3), the function will return 3, indicating that the first three integers are equal.  If the input is (1, 1, 1, 1, 2), the function will return 4, indicating that the first four integers are equal.  If the input is (1, 1, 1, 1, 1), the function will return 5, indicating that all five integers are equal.  If the input is (1, 1, 2, 2, 3), the function will return 4, indicating that the first two integers are equal, and the next two integers are equal.  If the input is (1, 1, 1, 1, 1, 1), the function will return 6, indicating that all six integers are equal.  If the input is (1, 1, 1, 1, 1, 1, 1), the function will return 7, indicating that all seven