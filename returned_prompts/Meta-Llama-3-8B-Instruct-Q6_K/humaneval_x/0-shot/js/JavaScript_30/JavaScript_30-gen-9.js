```javascript
const getPositive = (l) => l.filter(x => x > 0);
```
Explanation:
The `filter()` method creates a new array with all elements that pass the test implemented by the provided function. In this case, the function `x => x > 0` returns `true` for positive numbers and `false` for non-positive numbers. So, `filter()` will return a new array containing only the positive numbers from the original list.