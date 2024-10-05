  let left = 0, right = arr.length - 1;
  let changes = 0;

  while (left < right) {
    if (arr[left] != arr[right]) {
      changes++;
      let minIndex = left;
      if (arr[right] < arr[left]) {
        minIndex = right;
      }
      for (let i = left; i < right; i++) {
        if (arr[i] < arr[minIndex]) {
          minIndex = i;
        }
      }
      let temp = arr[minIndex];
      arr[minIndex] = arr[left];
      arr[left] = temp;
      right--;
    } else {
      left++;
      right--;
    }
  }

  return changes;
}