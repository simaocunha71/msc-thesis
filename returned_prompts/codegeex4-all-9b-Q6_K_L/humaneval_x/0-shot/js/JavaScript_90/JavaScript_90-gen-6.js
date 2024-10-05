Here's how you could solve this problem in JavaScript:

```javascript
const nextSmallest = (lst) => {
  // Check if list is empty or has less than 2 elements
  if (lst.length < 2) return null;
  
  // Create a copy of the list and sort it
  const sorted = [...lst].sort((a, b) => a - b);
  
  // Remove duplicates from the sorted list
  const unique = [...new Set(sorted)];
  
  // Check if there are at least 2 elements
  if (unique.length < 2) return null;
  
  // Return the 2nd smallest element
  return unique[1];
}
```

This function works by first checking if the list has fewer than 2 elements. If it does, it returns null since there's no 2nd smallest element.

Then, it creates a copy of the list and sorts it in ascending order. This is done using the `sort()` function with a compare function `(a, b) => a - b` to ensure numerical sorting rather than lexicographical.

Next, it removes duplicate elements from the sorted list using the `Set` object and the spread operator (`...`). This is done to ensure that the 2nd smallest element is unique.

Finally, it checks if there are at least 2 elements in the unique list. If not, it returns null. Otherwise, it returns the 2nd smallest element (`unique[1]`).

This solution assumes that the list can contain negative numbers and that the 2nd smallest element is unique. If the list can contain duplicate 2nd smallest elements, you would need to modify the function to return all such elements.