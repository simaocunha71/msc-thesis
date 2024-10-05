Here is the solution:

```javascript
const getPositive = (l) => l.filter(num => num > 0);
```



This function `getPositive` takes a list `l` as an argument and returns a new list with only the positive numbers from the original list. It does this by using the `filter` method, which creates a new list with all elements that pass the test implemented by the provided function. In this case, the function is `num => num > 0`, which returns `true` for numbers greater than 0 and `false` for numbers less than or equal to 0. The `filter` method then only includes the numbers for which the function returns `true`, effectively filtering out the non-positive numbers.