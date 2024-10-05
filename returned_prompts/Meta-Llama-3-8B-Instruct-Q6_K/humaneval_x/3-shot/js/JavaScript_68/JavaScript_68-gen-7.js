  let min_even = Infinity;
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < min_even) {
      min_even = arr[i];
      result = [min_even, i];
    }
  }
  return result.length === 0 ? [] : result;
}