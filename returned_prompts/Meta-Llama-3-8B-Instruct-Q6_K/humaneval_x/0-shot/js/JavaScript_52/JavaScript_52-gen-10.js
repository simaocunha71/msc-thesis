```javascript
const belowThreshold = (l, t) => l.every(num => num < t);
```



Explanation:

*   The `belowThreshold` function takes two arguments: a list `l` and a threshold `t`.
*   The function uses the `every` method, which returns `true` if all elements in the list satisfy a given condition.
*   The condition is specified as a lambda function `num => num < t`, which checks if each number in the list is less than the threshold `t`.
*   If all numbers in the list are below the threshold, the `every` method returns `true`; otherwise, it returns `false`.