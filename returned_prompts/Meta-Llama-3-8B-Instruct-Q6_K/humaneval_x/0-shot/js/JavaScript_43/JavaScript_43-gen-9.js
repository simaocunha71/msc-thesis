```
  return l.some((x, i, a) => a.some((y, j) => i !== j && x + y === 0));
```


Explanation:
The function `pairsSumToZero` checks if there are two distinct elements in the list that sum to zero. It uses the `some` method, which returns `true` if at least one element in the list satisfies the provided condition, and `false` otherwise.

The condition is defined as `(x + y === 0)`, which checks if the sum of two elements `x` and `y` is equal to zero.

The outer `some` loop iterates over the elements of the list, and for each element `x`, it checks if there is another element `y` in the list that satisfies the condition. The `i !== j` condition ensures that the two elements are distinct.

If the condition is satisfied for any pair of elements, the function returns `true`. If no such pair is found, the function returns `false`.