  if (arr.length === 0) {
    return true;
  }

  // Sort the array in ascending order
  arr.sort((a, b) => a - b);

  // Check if the array is sorted in non-decreasing order
  for (let i = 1; i < arr.length; i++) {
    if (arr[i - 1] > arr[i]) {
      return false;
    }
  }

  return true;
}



