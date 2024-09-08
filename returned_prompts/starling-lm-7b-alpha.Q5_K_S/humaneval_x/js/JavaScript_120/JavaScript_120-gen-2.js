  let result = [];
  let max = -Infinity;
  for (let i = 0; i < k; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] > max) {
        max = arr[j];
      }
    }
    result.push(max);
    max = -Infinity;
  }
  return result;
}



