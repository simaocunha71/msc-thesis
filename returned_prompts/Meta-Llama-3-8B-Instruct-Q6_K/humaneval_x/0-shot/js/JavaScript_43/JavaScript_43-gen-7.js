```
  return l.some((x, i) => l.some((y, j) => i !== j && x + y === 0));
```

Explanation:
The function `pairsSumToZero` checks if there are two distinct elements in the list that sum to zero. It uses the `some` method, which returns `true` if at least one element in the list matches the condition specified by the callback function.

The callback function takes two arguments, `x` and `y`, which represent two elements in the list. The condition `i !== j` ensures that `x` and `y` are distinct elements, and `x + y === 0` checks if the sum of `x` and `y` is equal to zero.

If the callback function returns `true` for any pair of elements, the `some` method returns `true`, indicating that there are two distinct elements that sum to zero. If the callback function returns `false` for all pairs of elements, the `some` method returns `false`, indicating that there are no two distinct elements that sum to zero.