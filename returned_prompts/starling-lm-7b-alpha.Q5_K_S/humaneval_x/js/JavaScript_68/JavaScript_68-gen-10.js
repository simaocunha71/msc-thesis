  let min_val = Number.MAX_VALUE;
  let min_val_index = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0 && arr[i] < min_val) {
      min_val = arr[i];
      min_val_index = i;
    }
  }
  return [min_val, min_val_index];
}



