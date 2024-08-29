  let max = arr[0];
  let index = 0;
  for (let i = 0; i < arr.length; i++) {
    if (max < arr[i]) {
      max = arr[i];
      index = i;
    }
  }
  for (let i = 0; i < index; i++) {
    let tmp = arr[i];
    arr[i] = arr[i + 1];
    arr[i + 1] = tmp;
  }
  return arr.every((val, idx) => val <= arr[idx + 1]);
}



