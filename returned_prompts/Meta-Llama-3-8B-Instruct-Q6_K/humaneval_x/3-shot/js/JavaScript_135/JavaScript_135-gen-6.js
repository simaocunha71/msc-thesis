  let result = -1;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= arr[i-1]) {
      result = i-1;
      break;
    }
  }
  return result;
}