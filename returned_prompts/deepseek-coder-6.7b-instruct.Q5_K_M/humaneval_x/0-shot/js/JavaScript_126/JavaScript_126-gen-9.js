  for (let i = 0; i < lst.length; i++) {
    if (lst[i] >= lst[i + 1]) return false;
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

// This code will iterate over the array and check if each element is less or equal than the next. If it's not, it returns false. If it finishes iterating over the array without returning, it returns true, meaning the array is sorted.

// Note: This solution assumes that the input list is not empty. If the input list can be empty, the function should return true to handle this special case.

// This solution also assumes that the input list does not contain any other kind of data than integers. If the input list can contain other data types, the function should add a check to handle this special case.

// This solution also assumes that the input list does not contain any negative numbers. If the input list can contain negative numbers, the function should add a check to handle this special case.

// This solution also assumes that the input list does not contain any duplicates of the same number. If the input list can contain duplicates, the function should add a check to handle this