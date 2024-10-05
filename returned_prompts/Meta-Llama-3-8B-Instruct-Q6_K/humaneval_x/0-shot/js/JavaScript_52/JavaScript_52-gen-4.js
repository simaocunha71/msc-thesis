```javascript
const belowThreshold = (l, t) => l.every(num => num < t);
```


Explanation:
The `every` method returns true if every element in the list satisfies the provided predicate (function). In this case, we provide a function that checks if the number is less than the threshold `t`. If any number in the list is not less than `t`, `every` will return `false`. Otherwise, it will return `true`. This is a concise and efficient way to check if all numbers in the list are below the threshold.