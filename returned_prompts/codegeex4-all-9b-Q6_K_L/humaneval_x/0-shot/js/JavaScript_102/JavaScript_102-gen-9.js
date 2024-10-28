```javascript
const chooseNum = (x, y) => {
  if (y < x) return -1;
  for (let i = Math.max(x, y); i >= Math.min(x, y); i--) {
    if (i % 2 === 0) return i;
  }
  return -1;
}
```

Explanation:
1. If y is less than x, then there is no such number in the range [x, y] and we return -1.
2. We use a loop to iterate through the numbers from the maximum of x and y down to the minimum of x and y.
3. If a number is even (i.e., it's divisible by 2 with no remainder), we return that number.
4. If we reach the end of the loop without finding an even number, we return -1.