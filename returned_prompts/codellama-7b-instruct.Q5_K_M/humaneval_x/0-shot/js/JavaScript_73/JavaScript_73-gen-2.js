const smallestChange = (arr) => {
  let result = 0;
  let left = 0;
  let right = arr.length - 1;
  let leftValue = arr[left];
  let rightValue = arr[right];
  while (left < right) {
    if (leftValue !== rightValue) {
      result++;
      leftValue = arr[left];
      rightValue = arr[right];
    }
    left++;
    right--;
  }
  return result;
};
