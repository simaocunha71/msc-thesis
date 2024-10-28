  if (k == 0) {
    return [];
  }
  let result = [];
  let max = 0;
  let max_index = 0;
  for (let i = 0; i < k; i++) {
    max = -1000;
    for (let j = i; j < arr.length; j++) {
      if (arr[j] > max) {
        max = arr[j];
        max_index = j;
      }
    }
    result.push(max);
    arr[max_index] = -1000;
  }
  return result;
}