To solve this problem, you can follow these steps:

1. Define the function `sortEven` that takes a list `l` as an argument.
2. Create a new list `l_sorted` that will store the sorted values of even indices of `l`.
3. Iterate through `l` using the `forEach` method. For each element `el` at index `i`, check if `i` is an even number using the modulo operator `%`. If `i` is even, push `el` into `l_sorted`.
4. Sort `l_sorted` using the `sort` method. This will sort the values at even indices of `l`.
5. Use the `map` method to iterate through `l` again. For each element `el` at index `i`, check if `i` is an even number using the modulo operator `%`. If `i` is even, replace `el` with the corresponding element from `l_sorted`.
6. Return the modified `l`.

Here is the code for the solution:

```javascript
const sortEven = (l) => {
  const l_sorted = l.filter((_, i) => i % 2 === 0).sort((a, b) => a - b);
  return l.map((el, i) => i % 2 === 0 ? l_sorted[i / 2] : el);
};
```

This implementation uses the `filter` method to separate the even elements of `l` into `l_sorted`. The `sort` method is then used to sort `l_sorted`. Finally, the `map` method is used to replace the even elements of `l` with the sorted elements from `l_sorted`.

The time complexity of this solution is O(n log n), where n is the length of the input list `l`. This is because the `sort` method has a time complexity of O(n log n).

The space complexity of this solution is O(n), where n is the length of the input list `l`. This is because we are creating a new list `l_sorted` to store the sorted values of even indices.

Overall, this solution provides an efficient way to sort the values at even indices of a given