```javascript
const chooseNum = (x, y) => {
  // Check if the range is valid
  if (x > y) return -1;

  // Find the biggest even number in the range
  for (let i = y; i >= x; i--) {
    if (i % 2 === 0) return i;
  }

  // If no even number is found, return -1
  return -1;
}
```

Explanation:
1. The function `chooseNum` takes two arguments `x` and `y`.
2. It checks if the range `[x, y]` is valid. If `x` is greater than `y`, it returns `-1`.
3. It then iterates from `y` to `x` and checks if each number is even. If it finds an even number, it returns that number.
4. If no even number is found, it returns `-1`.