```javascript
const belowThreshold = (l, t) => l.every(n => n < t);
```


Explanation:
The function `belowThreshold` takes two arguments, `l` (a list of numbers) and `t` (a threshold). It uses the `every` method, which returns `true` if all elements in the list satisfy the provided condition. In this case, the condition is `n < t`, which checks if each number `n` in the list is less than the threshold `t`. If all numbers are below the threshold, the function returns `true`; otherwise, it returns `false`. This solution is concise, efficient, and easy to understand.