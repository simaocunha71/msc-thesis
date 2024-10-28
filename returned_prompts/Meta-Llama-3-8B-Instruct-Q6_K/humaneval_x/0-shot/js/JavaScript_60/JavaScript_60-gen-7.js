```javascript
const sumToN = (n) => {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
};
```


This function uses a for loop to iterate from 1 to n, and at each iteration, it adds the current number to a running total. The total is then returned. The time complexity of this function is O(n), because it needs to iterate n times. The space complexity is O(1), because it only uses a constant amount of space.