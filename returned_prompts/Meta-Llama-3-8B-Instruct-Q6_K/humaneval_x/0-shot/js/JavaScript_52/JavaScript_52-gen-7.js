```
const belowThreshold = (l, t) => l.every(x => x < t);
```


Explanation:
The function `belowThreshold` takes two arguments: `l`, a list of numbers, and `t`, a threshold. It returns a boolean indicating whether all numbers in `l` are below the threshold `t`.

The function uses the `every` method, which returns `true` if all elements in the list satisfy a given condition. In this case, the condition is `x < t`, which checks if each number `x` in the list is less than the threshold `t`.

The `every` method stops iterating as soon as it finds an element that does not satisfy the condition, so if there is even one number in the list that is not below the threshold, the method will return `false`. If all numbers are below the threshold, the method will return `true`.