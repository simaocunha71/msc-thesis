Here's one way to solve this problem:

```javascript
const isSorted = (lst) => {
  // Check if the length of the list is less than 2. If it is, return true since there's only one element, which is considered sorted.
  if (lst.length < 2) return true;

  // Iterate through the list starting from the second element.
  for (let i = 1; i < lst.length; i++) {
    // If the current element is less than the previous element, return false since the list is not sorted in ascending order.
    if (lst[i] < lst[i - 1]) return false;
  }

  return true;
};
```

This solution uses a for loop to iterate through the list starting from the second element. It compares each element with its previous element. If the current element is less than the previous element, it means the list is not sorted in ascending order, and the function returns false. If the loop completes without finding any out-of-order elements, it means the list is sorted, and the function returns true.

This solution also handles the case where the list has more than one duplicate of the same number. Since the function only cares about the relative order of the elements, it doesn't matter if there are duplicates. The function will still return true as long as all elements are in ascending order relative to each other.

Here are some examples of how the function can be used:

```javascript
console.log(isSorted([5]));       // true
console.log(isSorted([1, 2, 3, 4, 5]));  // true
console.log(isSorted([1, 3, 2, 4, 5]));   // false
console.log(isSorted([1, 2, 3, 4, 5, 6])); // true
console.log(isSorted([1, 2, 3, 4, 5, 6, 7])) // true
console.log(isSorted([1, 3, 2, 4, 5, 6, 7])) // false
console.log(isSorted([1, 