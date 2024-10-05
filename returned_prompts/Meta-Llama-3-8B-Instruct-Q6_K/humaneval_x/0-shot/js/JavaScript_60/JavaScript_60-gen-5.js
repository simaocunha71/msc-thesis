```
const sumToN = (n) => {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}
```
This function uses a for loop to iterate from 1 to n, and for each iteration, it adds the current number to a running total (initially set to 0). The final total is returned. This is a simple and straightforward implementation of the sum of the first n natural numbers.