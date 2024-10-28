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
This function uses a for loop to iterate from 1 to n, and adds each number to a running total. The total is returned at the end of the function. The sum of all numbers from 1 to n is known as the nth triangular number, which can be calculated using the formula n*(n+1)/2. However, for the purposes of this exercise, a simple for loop is used. The function takes an integer n as input and returns the sum of all numbers from 1 to n.