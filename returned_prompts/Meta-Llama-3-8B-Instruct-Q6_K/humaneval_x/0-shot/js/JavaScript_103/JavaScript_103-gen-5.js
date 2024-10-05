Here is a JavaScript solution for the problem:

```javascript
const roundedAvg = (n, m) => {
  if (n > m) return -1;

  let sum = 0;
  for (let i = n; i <= m; i++) {
    sum += i;
  }

  let avg = Math.round(sum / (m - n + 1));
  return avg.toString(2);
};
```

This function first checks if n is greater than m, and if so, returns -1. Then it calculates the sum of the integers from n to m using a for loop. It calculates the average by dividing the sum by the number of integers (m - n + 1), rounds the average to the nearest integer using the Math.round function, and then converts the average to a binary string using the toString function with a base of 2. The result is returned as a string.