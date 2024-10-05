```javascript
const common = (l1, l2) => {
  let uniqueCommon = [...new Set(l1.filter(x => l2.includes(x)))];
  return uniqueCommon.sort((a, b) => a - b);
};
```


Explanation:
This function takes two lists `l1` and `l2` as input. It uses the `filter` method to create a new array with elements that are present in both lists. The `includes` method is used to check if an element is present in the second list. The `Set` data structure is used to remove duplicates from the filtered array.

Then, it returns the sorted unique common elements using the `sort` method. The `sort` method sorts the array in ascending order by default. The arrow function `(a, b) => a - b` is used to specify the sorting order as ascending.

The time complexity of this solution is O(n log n) due to the sorting operation, where n is the length of the input lists. The space complexity is O(n) for storing the unique common elements.