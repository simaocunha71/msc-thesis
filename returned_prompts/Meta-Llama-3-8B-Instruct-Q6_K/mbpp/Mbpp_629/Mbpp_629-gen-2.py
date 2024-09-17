```
def find_even_numbers(lst):
    return [i for i in lst if i % 2 == 0]
```
This function uses a list comprehension to iterate over each number in the input list `lst`. It checks if the number is even by using the modulus operator `%`, which returns the remainder of the division of the number by 2. If the remainder is 0, the number is even. The even numbers are then added to a new list, which is returned by the function.

For example, if the input list is `[1, 2, 3, 4, 5]`, the function will return `[2, 4]`, which are the even numbers in the list.

The unit test `assert Split([1,2,3,4,5]) == [2,4]` ensures that the function is working correctly. It checks that the output of the function is equal to the expected output `[2,4]` when the input is `[1,2,3,4,5]`. If the function is working correctly, the assertion will pass; otherwise, it will raise an AssertionError.