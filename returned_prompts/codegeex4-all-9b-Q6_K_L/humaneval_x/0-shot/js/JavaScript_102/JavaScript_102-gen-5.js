```javascript
const chooseNum = (x, y) => {
  const range = [];
  for (let i = x; i <= y; i++) {
    range.push(i);
  }
  const evens = range.filter(num => num % 2 === 0);
  if (evens.length > 0) {
    return Math.max(...evens);
  } else {
    return -1;
  }
}
```

Explanation:
The function `chooseNum` takes two positive numbers `x` and `y` as input. It creates an array `range` containing all the numbers in the range `[x, y]` inclusive. Then, it filters the array to get only the even numbers and stores them in the `evens` array. If the length of `evens` is greater than 0, it returns the maximum number from `evens` using `Math.max`. Otherwise, it returns -1.