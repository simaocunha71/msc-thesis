  if (arr.length === 0) return true;
  let max = arr[0];
  let index = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < max) {
      if (arr[i] > arr[index]) {
        index = i;
      }
    } else {
      max = arr[i];
    }
  }
  if (index + 1 >= arr.length) return true;
  const tmp = arr[arr.length - 1];
  for (let i = arr.length - 2; i >= index; i--) {
    arr[i + 1] = arr[i];
  }
  arr[index] = tmp;
  return moveOneBall(arr);
}



