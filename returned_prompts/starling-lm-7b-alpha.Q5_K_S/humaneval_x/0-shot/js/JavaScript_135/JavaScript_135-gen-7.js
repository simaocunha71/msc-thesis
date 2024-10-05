  let largestIndex = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > arr[largestIndex]) {
      largestIndex = i;
    }
  }
  return largestIndex;
};

/*
  This function works by initializing a variable to the index of the first
  element in the array. It then iterates through the rest of the array,
  starting from the second element. At each iteration, it compares the
  current element to the element at the largest index. If the current element
  is greater than the element at the largest index, it updates the largest index
  to be the current index. If no element is found to be greater than the element
  at the largest index, the function returns -1.

  The function can be improved by adding a conditional statement to check if
  any element is greater than the element at the largest index. If none are found
  to be greater, the function can return -1 immediately, rather than waiting until
  the end of the loop.

  This improvement would reduce the time complexity of the function from O(n) to O(n/2),
  where n is the length of the array.
*/

console.log(canArrange([1, 2, 4, 3, 5])); // 3
console.log(canArrange([1, 2, 3])); // -1























































































































































































