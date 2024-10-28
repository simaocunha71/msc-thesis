```javascript
const getPositive = (l) => l.filter(n => n > 0);
```


Explanation:
The function `getPositive` takes a list `l` as input and returns a new list containing only the positive numbers from the original list. This is achieved by using the `filter` method, which creates a new array with all elements that pass the test implemented by the provided function.

In this case, the function `n => n > 0` is used as the test. This function takes an element `n` from the list and returns a boolean indicating whether `n` is greater than 0. The `filter` method then applies this test to each element in the list and returns a new array containing only the elements for which the test returns `true`, i.e., the positive numbers.

For example, given the list `[-1, 2, -4, 5, 6]`, the function `getPositive` would return the list `[2, 5, 6]`, which contains only the positive numbers from the original list. Similarly, given the list `[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]`, the function `getPositive` would return the list `[5, 3, 2, 3, 9, 123, 1]`, which contains only the positive numbers from the original list.