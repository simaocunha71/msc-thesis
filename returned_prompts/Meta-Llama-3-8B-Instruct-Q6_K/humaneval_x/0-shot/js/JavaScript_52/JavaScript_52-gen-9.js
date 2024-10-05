```javascript
const belowThreshold = (l, t) => l.every(x => x < t);
```
Explanation:
The `every()` method is used to check if all elements in the list `l` satisfy the condition `x < t`. It returns `true` if all elements satisfy the condition, and `false` otherwise. The condition `x < t` checks if each number `x` in the list is below the threshold `t`. If all numbers are below the threshold, the method returns `true`, otherwise it returns `false`.