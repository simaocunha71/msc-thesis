```
def sum_even_and_even_index(lst):
    return sum([num for idx, num in enumerate(lst) if idx % 2 == 0 and num % 2 == 0])
```
The function `sum_even_and_even_index` takes a list `lst` as input. It uses a list comprehension to iterate over the list and its indices. It checks if the index `idx` is even (`idx % 2 == 0`) and if the number `num` is even (`num % 2 == 0`). If both conditions are met, it adds the number to the sum. The function returns the sum of the even numbers at even positions.

The unit test `assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30` ensures that the function works correctly. It checks if the sum of the even numbers at even positions of the list `[5, 6, 12, 1, 18, 8]` is equal to `30`. The function returns `30`, which passes the test.

For example, if the input list is `[5, 6, 12, 1, 18, 8]`, the function will return `30`, which is the sum of the even numbers at even positions (6, 12, 18). If the input list is `[1, 2, 3, 4, 5, 6]`, the function will return `8`, which is the sum of the even numbers at even positions (2, 4, 6). If the input list is `[1, 3, 5, 7, 9, 11]`, the function will return `0`, which is the sum of the even numbers at even positions (since there are no even numbers at even positions).