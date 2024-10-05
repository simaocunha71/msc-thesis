```
const getPositive = (l) => l.filter(num => num > 0);
```


Explanation:
The problem is asking to write a function that takes a list of numbers as an argument and returns a new list containing only the positive numbers from the original list.

The solution uses the `filter()` method, which is a built-in method in JavaScript that creates a new array with all elements that pass the test implemented by the provided function. In this case, the function `num => num > 0` returns `true` for numbers greater than 0 and `false` for numbers less than or equal to 0. This effectively filters out all the non-positive numbers from the original list.

For example, if the input list is `[-1, 2, -4, 5, 6]`, the `filter()` method will iterate over the list, check each number, and return a new list containing only the numbers that are greater than 0, which are `[2, 5, 6]`.

The resulting list is then returned by the `getPositive()` function.