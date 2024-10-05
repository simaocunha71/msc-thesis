  let result = true;
  arr = arr.slice().sort((a, b) => a - b);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== i + 1) {
      result = false;
      break;
    }
  }
  return result;
}