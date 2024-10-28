  const arr1 = l1.sort((a, b) => a - b);
  const arr2 = l2.sort((a, b) => a - b);

  const result = [];

  for (let i = 0; i < arr1.length; i++) {
    if (arr2.includes(arr1[i]) && !result.includes(arr1[i])) {
      result.push(arr1[i]);
    }
  }

  return result;
}

console.log(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]));
console.log(common([5, 3, 2, 8], [3, 2]));

```

## Code Explanation

- This program takes in two arrays (l1 and l2) and returns the common elements in a sorted order.
- The first step of the program is to sort the arrays in ascending order.
- Then it iterates over the first array (arr1). For each element in arr1, it checks if this element is also in arr2 and not already in the result array. If these conditions are met, this element is added to the result array.
- Finally, the result array is returned.
- The solution is in JavaScript.

## Complexity

- Time Complexity: O(n log n) due to sorting, where n is the length of the longest array.
- Space Complexity: O(n) since in the worst case scenario, all elements from the longer array might end up in the result.

## Other approaches

- Another approach is to use Sets and the `filter` method to find common elements. This approach could be more readable and performant in some cases.

```js
const common = (l1, l2) => {
  const set1 = new Set(l1);
  const set2 = new Set(l2);
  return [...new Set([...set1].filter(v => set2.has(v)))]
};
```

- This approach uses ES6 Set objects, which