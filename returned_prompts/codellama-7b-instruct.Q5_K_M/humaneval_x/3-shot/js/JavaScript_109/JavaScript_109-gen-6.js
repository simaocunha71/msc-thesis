  // first, sort array
  arr.sort((a, b) => a - b);
  // second, check if the array is already sorted
  if (arr[0] <= arr[arr.length - 1]) {
    return true;
  }
  // third, check if the array can be sorted by shifting elements
  for (let i = 1; i < arr.length; i++) {
    // check if the previous element is less than the current element
    if (arr[i] < arr[i - 1]) {
      // shift the current element to the end of the array
      arr.push(arr.shift());
      // check if the array is sorted
      if (arr[0] <= arr[arr.length - 1]) {
        return true;
      }
      // check if the array can be sorted by shifting the elements again
      i--;
    }
  }
  return false;
}



