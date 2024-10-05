```javascript
const sumToN = (n) => {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
};
```


Explanation:
The function sumToN takes an integer n as an argument and returns the sum of all integers from 1 to n. It uses a for loop to iterate over the range from 1 to n, adding each number to a running total sum. The sum is then returned at the end of the function. The function is defined using the arrow function syntax, which is a concise way to define small functions in JavaScript. The function can be called with different values of n, such as 30, 100, 5, 10, or 1, and will return the correct sum for each case. For example, sumToN(30) returns 465, sumToN(100) returns 5050, and so on.