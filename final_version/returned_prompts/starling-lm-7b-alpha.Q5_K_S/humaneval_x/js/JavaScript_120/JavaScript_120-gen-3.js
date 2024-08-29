  let result = [];
  arr.sort((a, b) => {
    return b - a;
  });
  for (let i = 0; i < k; i++) {
    result.push(arr[i]);
  }
  return result;
}



