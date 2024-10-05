```
const getPositive = (l) => l.filter(n => n > 0);
```


Explanation:
The task is to create a function that takes a list of numbers as input and returns a new list containing only the positive numbers from the original list.

The solution uses the built-in `filter()` method, which creates a new array with all elements that pass the test implemented by the provided function.

In this case, the function `n => n > 0` is used to filter the list. This function returns `true` for any number `n` that is greater than 0, and `false` otherwise. The `filter()` method then uses these boolean values to decide which elements to include in the new list.

For example, if the input list is `[-1, 2, -4, 5, 6]`, the `filter()` method will return a new list containing only the numbers that are greater than 0, which are `[2, 5, 6]`.