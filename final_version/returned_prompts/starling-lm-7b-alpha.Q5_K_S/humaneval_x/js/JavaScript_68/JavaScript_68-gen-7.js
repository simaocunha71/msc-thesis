  let result = [Infinity, 0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0 && arr[i] < result[0]) {
      result = [arr[i], i];
    }
  }
  if (result[0] === Infinity) {
    return [];
  }
  return result;
}



