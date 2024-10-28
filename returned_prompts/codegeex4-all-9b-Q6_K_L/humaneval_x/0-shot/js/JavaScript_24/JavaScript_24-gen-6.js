The following JavaScript function can solve this problem:

```javascript
const largestDivisor = (n) => {
  for (let i = n - 1; i > 1; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return n;
}
```

This function starts from n - 1 and goes down to 2. It checks each number to see if it divides n evenly (i.e., n % i === 0). When it finds a number that divides n evenly, it returns that number. If no numbers divide n evenly, the function returns n.