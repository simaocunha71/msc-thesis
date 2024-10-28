Here's how you might do it in JavaScript:

```javascript
const common = (l1, l2) => {
  const set1 = new Set(l1);
  const set2 = new Set(l2);
  const commonElements = Array.from(set1).filter(x => set2.has(x));
  return commonElements.sort((a, b) => a - b);
}
```

In this function, we first create two sets from the two input lists. A set is a collection of unique elements, so this removes duplicates.

Then we create a new array from the first set using `Array.from()`, and filter out any elements that are not in the second set. This gives us an array of the common elements.

Finally, we use the `sort()` method to sort the array in ascending order.

This function should work for any two lists of numbers, and it will return a sorted list of unique common elements.

Do note that the sort function would not work for strings. If you are dealing with strings, you can replace `(a, b) => a - b` with `(a, b) => a.localeCompare(b)` in the sort function.