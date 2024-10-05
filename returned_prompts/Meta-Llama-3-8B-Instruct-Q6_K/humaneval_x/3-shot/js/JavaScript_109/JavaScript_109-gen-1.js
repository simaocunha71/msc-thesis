  if (arr.length === 0) {
    return true;
  }

  let minIndex = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[minIndex]) {
      minIndex = i;
    }
  }

  let rotations = minIndex;
  for (let i = 0; i < rotations; i++) {
    arr.push(arr.shift());
  }

  return arr.every((val, i) => val <= arr[i + 1]);
} // O(n) time complexity and O(1) space complexity
// This function works by first finding the index of the smallest element in the array.
// Then it performs the necessary number of right shifts to move this element to the front of the array.
// Finally it checks if the array is sorted in non-decreasing order.