```javascript
const getPositive = (list) => list.filter((num) => num > 0);
```



The function `getPositive` takes a list of numbers as an argument and returns a new list containing only the positive numbers from the original list. The `filter` method is used to achieve this. It creates a new array with all elements that pass the test implemented by the provided function.

The provided function is a lambda function `(num) => num > 0` that returns `true` if the number is positive and `false` otherwise. The `filter` method applies this function to each element in the list and includes the element in the new array if the function returns `true`. This effectively filters out the non-positive numbers.

For example, if the input list is `[-1, 2, -4, 5, 6]`, the `filter` method will return a new list containing only the positive numbers: `[2, 5, 6]`. If the input list is `[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]`, the `filter` method will return a new list containing only the positive numbers: `[5, 3, 2, 3, 9, 123, 1]`.