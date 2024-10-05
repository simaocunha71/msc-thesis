```
  return l.some((x, i) => l.includes(-x) && i !== l.indexOf(-x));
```
This function uses the `some` method to check if at least one element in the list satisfies the condition. The condition is that the element `x` is included in the list and its index `i` is not equal to the index of its negation `-x`. This ensures that we are finding distinct pairs that sum to zero.

For example, in the list `[2, 4, -5, 3, 5, 7]`, the element `-5` is included in the list and its index is not equal to the index of its negation `5`. Therefore, the function returns `true`.

Note that this function assumes that the input list does not contain duplicate elements. If the list can contain duplicates, you may want to use a different approach, such as using a `Set` to keep track of the elements you have seen so far.