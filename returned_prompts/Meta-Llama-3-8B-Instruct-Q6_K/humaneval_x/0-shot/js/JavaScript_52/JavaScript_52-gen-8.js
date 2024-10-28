```
  return l.every(x => x < t);
```
Explanation:
The `every` method is used to check if all elements in the array `l` satisfy the condition `x < t`. If any element is not below the threshold `t`, `every` will return `false`. If all elements are below the threshold, `every` will return `true`. 

This function works because `every` will stop checking as soon as it finds an element that does not satisfy the condition, so it's more efficient than checking all elements and then returning a boolean. 

For example, in the case of `belowThreshold([1, 2, 4, 10], 100)`, `every` will check `1 < 100`, `2 < 100`, `4 < 100`, and `10 < 100`, and since all of these are true, it will return `true`. 

In the case of `belowThreshold([1, 20, 4, 10], 5)`, `every` will check `1 < 5`, `20 < 5`, `4 < 5`, and `10 < 5`, and since `20` is not below 5, it will return `false`. 