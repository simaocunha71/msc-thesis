```javascript
const doubleTheDifference = (lst) => {
  let sum = 0;
  lst.filter(num => typeof num === 'number' && num >= 0 && num % 1 === 0 && num % 2 !== 0)
    .map(num => num ** 2)
    .forEach(num => sum += num);
  return sum;
};
```


Explanation:
We use the `filter` method to select the numbers that are non-negative integers, and then the `map` method to square each number. The `forEach` method is used to add each squared number to the `sum`. Finally, the `return` statement returns the `sum`. The `filter` condition is `num >= 0 && num % 1 === 0 && num % 2 !== 0`, which ensures that the number is non-negative, an integer, and odd. If the input list is empty, the function returns 0 as per the problem statement.