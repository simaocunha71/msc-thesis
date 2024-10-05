Here is the solution:
```
const sortEven = (l) => {
  return l.map((x, i) => i % 2 === 0 ? [...l.slice(0, i)].flat().sort((a, b) => a - b)[0] : x);
};
```
Here's an explanation of the code:

* `l.map()` creates a new list by applying a transformation to each element of the original list.
* `x, i)` are the current element and its index, respectively.
* `i % 2 === 0` checks if the index is even (i.e., the element is at an even position in the list).
* If the index is even, we use the `slice()` method to get all elements before the current one, `flat()` to flatten the resulting array (since `slice()` returns an array of arrays), and `sort()` to sort the elements. We then take the first element of the sorted array (which is the smallest element).
* If the index is odd, we simply return the original element `x`.
* The resulting list is returned by the `map()` method.