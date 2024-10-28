  const palindrome = (arr) => {
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
      if (arr[left] !== arr[right]) {
        return false;
      }
      left++;
      right--;
    }
    return true;
  };

  if (palindrome(arr)) {
    return 0;
  }

  // Find the minimum number of elements to change
  let min = Infinity;
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] !== arr[j]) {
        min = Math.min(min, Math.abs(arr[i] - arr[j]));
      }
    }
  }
  return min;
};
