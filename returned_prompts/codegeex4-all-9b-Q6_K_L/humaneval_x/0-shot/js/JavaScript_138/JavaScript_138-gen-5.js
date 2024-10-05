You can solve this problem using the following approach:

1. Check if n is even. If not, return false.
2. Check if n is less than 8. If it is, return false.
3. Check if (n - 8) is even. If it is, return true. Otherwise, return false.

Here is the code for the function:

```javascript
const isEqualToSumEven = (n) => {
  if (n % 2 !== 0) {
    return false;
  }
  if (n < 8) {
    return false;
  }
  return (n - 8) % 2 === 0;
}
```

This function first checks if n is even. If not, it immediately returns false. Then it checks if n is less than 8. If it is, it returns false. Finally, it checks if (n - 8) is even. If it is, it returns true. Otherwise, it returns false.