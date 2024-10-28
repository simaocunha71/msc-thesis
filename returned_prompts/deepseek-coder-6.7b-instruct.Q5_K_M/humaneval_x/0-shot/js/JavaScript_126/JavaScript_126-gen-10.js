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


## Answer
The function isSorted checks if the array is sorted in ascending order. If the next number in the array is smaller than the current number, it returns false, because the array is not sorted. If the function manages to iterate through the entire array without finding any such pair, it returns true, because the array is sorted.

The function also checks if there are more than one identical numbers in the array. If it does, the function will return false, because array with more than one identical numbers is not sorted.

In each iteration of the loop, the function compares the current number with the next one. If the current number is greater than or equal to the next one, the function returns false. If the function manages to iterate through the entire array without returning false, it means that the array is sorted and the function returns true.

The function does not use any built-in sorting functions. It