```javascript
const nextSmallest = (lst) => {
  // Edge case: if the list is empty or has less than 2 elements, return null
  if (lst.length < 2) return null;

  // Create a copy of the list and sort it in ascending order
  const sorted = [...lst].sort((a, b) => a - b);

  // Remove duplicate elements by converting the sorted array to a Set, then back to an array
  const unique = [...new Set(sorted)];

  // If the length of the unique array is less than 2, return null
  if (unique.length < 2) return null;

  // Return the 2nd smallest element
  return unique[1];
}
```
