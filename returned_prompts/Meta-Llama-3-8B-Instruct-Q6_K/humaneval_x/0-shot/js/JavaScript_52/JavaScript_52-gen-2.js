```
const belowThreshold = (l, t) => l.every(x => x < t);
```


Explanation:
The `every` method is used to check if all elements in the list `l` satisfy the condition `x < t`. If any element does not satisfy this condition, the method will return `false`. If all elements satisfy the condition, the method will return `true`.

Example:
`belowThreshold([1, 2, 4, 10], 100)` will return `true` because all numbers in the list are below 100.

`belowThreshold([1, 20, 4, 10], 5)` will return `false` because the number 20 is not below 5.