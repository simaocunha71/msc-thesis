  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= arr[i - 1]) {
      return i - 1;
    }
  }
  return -1;
}
// The above function returns the largest index of an element which is not greater than or equal to the element immediately preceding it. If no such element exists then return -1. The given array will not contain duplicate values. The function works by iterating through the array from left to right and checking if each element is less than or equal to the previous element. If such an element is found, its index is returned. If no such element is found after iterating through the entire array, the function returns -1. This approach ensures that the function returns the largest index of an element which is not greater than or equal to the element immediately preceding it, as required by the problem.