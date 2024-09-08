  let result = -1;
  for (let i = 0; i < arr.length; i++) {
    if (i > 0 && arr[i] > arr[i-1]) {
      return result;
    } else {
      result = i;
    }
  }
  return result;
}



