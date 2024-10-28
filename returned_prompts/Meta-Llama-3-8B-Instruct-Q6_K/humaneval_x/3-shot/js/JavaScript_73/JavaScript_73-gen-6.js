  let n = arr.length;
  let count = 0;
  let left = 0;
  let right = n - 1;
  let leftArr = [];
  let rightArr = [];

  while (left <= right) {
    if (arr[left] != arr[right]) {
      leftArr.push(arr[left]);
      rightArr.push(arr[right]);
      count++;
    } else {
      left++;
      right--;
    }
  }

  return count;
}
