  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] >= lst[i + 1]) {
      return false;
    }
  }

  return true;
}

console.log(isSorted([5])); // ➞ true
console.log(isSorted([1, 2, 3, 4, 5])); // ➞ true
console.log(isSorted([1, 3, 2, 4, 5])); // ➞ false
console.log(isSorted([1, 2, 3, 4, 5, 6])); // ➞ true
console.log(isSorted([1, 2, 3, 4, 5, 6, 7])); // ➞ true
console.log(isSorted([1, 3, 2, 4, 5, 6, 7])); // ➞ false
console.log(isSorted([1, 2, 2, 3, 3, 4])); // ➞ true
console.log(isSorted([1, 2, 2, 2, 3, 4])); // ➞ false
```

## Solution:

This solution works by iterating through the array and checking if each element is less than or equal to the next one. If it is, the function continues. If it isn't, the function returns false. If the function has checked all elements without finding one that isn't in ascending order, it returns true.

The time complexity of this solution is O(n), where n is the length of the array, as it has to iterate through the array once. The space complexity is O(1), as it only needs a single variable to keep track of the current element and the next one.

The function isSorted is a simple and efficient way to check if a list of numbers is sorted in ascending order.

```js
const isSorted = (lst) => {
  for (let i = 0; i < lst.length - 1; i++) {
