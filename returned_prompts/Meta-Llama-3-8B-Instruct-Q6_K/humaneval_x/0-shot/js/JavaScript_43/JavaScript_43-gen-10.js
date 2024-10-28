```
const pairsSumToZero = (l) => {
  return l.some((x, i) => l.includes(-x) && i !== l.indexOf(-x));
};
```


Explanation:
The function `pairsSumToZero` takes a list of integers `l` as an input. It returns `true` if there are two distinct elements in the list that sum to zero, and `false` otherwise.

The function uses the `some` method, which returns `true` if at least one element in the list satisfies the provided condition, and `false` otherwise.

The condition is: `l.includes(-x) && i !== l.indexOf(-x)`.

This condition checks if there is an element `-x` in the list `l`, and if it's not the same element `x` itself (to ensure distinct elements). If such an element is found, the function returns `true`.

For example, in the list `[2, 4, -5, 3, 5, 7]`, the function will find the pair `-5` and `5`, which sum to zero, and return `true`. In other lists, it will not find such a pair, and return `false`.