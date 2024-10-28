Here is the solution for the problem:

```javascript
const common = (l1, l2) => {
  const set1 = new Set(l1);
  const set2 = new Set(l2);
  const intersection = new Set([...set1].filter(x => set2.has(x)));
  return Array.from(intersection).sort((a, b) => a - b);
};
```

Explanation:
The problem asks to find the common elements between two lists and return them in a sorted manner. We use the `Set` data structure to find the common elements. 

First, we convert the lists to sets. Then, we use the `filter` method to find the elements that exist in both sets. We convert the resulting set back to an array and sort it. 

The `Set` data structure automatically removes duplicates, so we don't need to worry about that. The `filter` method allows us to find the elements that exist in both sets, and the `sort` method sorts the resulting array. 

The `Array.from` method is used to convert the set to an array. The `sort` method is used to sort the array in ascending order. 

The function `common` takes two lists as arguments and returns the sorted unique common elements. 

For example, if we call `common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])`, it will return `[1, 5, 653]`. If we call `common([5, 3, 2, 8], [3, 2])`, it will return `[2, 3]`. 