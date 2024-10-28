```
const sumToN = (n) => {
  let total = 0;
  for (let i = 1; i <= n; i++) {
    total += i;
  }
  return total;
};
```


Explanation:
The function sumToN takes an integer n as an argument and returns the sum of all integers from 1 to n. It uses a for loop to iterate from 1 to n, adding each integer to a variable total. The function then returns the total. This function will work for any positive integer n. For example, sumToN(30) will return 465, which is the sum of the numbers from 1 to 30. Similarly, sumToN(100) will return 5050, which is the sum of the numbers from 1 to 100.