  if (arr.length === 0) {
    return true;
  }
  let max = arr[0];
  let count = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < max) {
      count++;
    } else {
      max = arr[i];
    }
  }
  return count <= 1;
}