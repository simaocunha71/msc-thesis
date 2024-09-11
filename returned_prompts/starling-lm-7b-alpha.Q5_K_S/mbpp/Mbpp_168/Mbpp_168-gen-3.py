```
def frequency(lst, num):
    count = 0
    for i in lst:
        if i == num:
            count += 1
    return count
```

Explanation:

This function `frequency` takes in a list `lst` and a number `num` as arguments. It initializes a variable `count` to 0, which will be used to keep track of the number of occurrences of `num` in `lst`. 

The function then iterates through each element `i` in `lst`. If `i` is equal to `num`, it increments `count` by 1. 

After iterating through all the elements in `lst`, the function returns the final value of `count`, which represents the number of occurrences of `num` in `lst`.

The provided assertion `assert frequency([1,2,3], 4) == 0` asserts that when the function `frequency` is called with the list `[1,2,3]` and the number `4`, the result should be `0`, indicating that `4` does not appear in the list.

This function can be used to count the occurrences of any number in a given list.

Here's an example usage of the function:

```python
my_list = [1, 2, 3, 2, 4, 2, 5, 2]
number_to_count = 2
result = frequency(my_list, number_to_count)
print(result)  # Output: 4
```

In this example, the function `frequency` is called with the list `[1, 2, 3, 2, 4, 2, 5, 2]` and the number `2`. The function returns `4`, indicating that the number `2` appears four times in the list.

Note that the function `frequency` is case-sensitive and does not handle duplicate occurrences of the same number.

You can modify the function to handle duplicate occurrences by using a dictionary to keep track of the count for each number, like this:

```python
def frequency(lst, num):
    count_dict = {}
    for i in l