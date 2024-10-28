  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] >= lst[i + 1]) {
      return false;
    }
  }
  return true;
};

console.log(isSorted([5])); // ➞ true
console.log(isSorted([1, 2, 3, 4, 5])); // ➞ true
console.log(isSorted([1, 3, 2, 4, 5])); // ➞ false
console.log(isSorted([1, 2, 3, 4, 5, 6])); // ➞ true
console.log(isSorted([1, 2, 3, 4, 5, 6, 7])); // ➞ true
console.log(isSorted([1, 3, 2, 4, 5, 6, 7])); // ➞ false
console.log(isSorted([1, 2, 2, 3, 3, 4])); // ➞ true
console.log(isSorted([1, 2, 2, 2, 3, 4])); // ➞ false

```

The solution is to iterate through the array and check each element to see if it is greater than or equal to the next one. If it is, return false. If the function finishes without returning false, then the array must be sorted in ascending order, so return true.













































































































































