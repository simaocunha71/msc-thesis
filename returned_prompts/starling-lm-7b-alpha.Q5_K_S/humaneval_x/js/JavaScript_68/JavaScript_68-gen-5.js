  let min_even_val = Infinity;
  let min_even_index = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < min_even_val) {
      min_even_val = arr[i];
      min_even_index = i;
    }
  }
  return [min_even_val, min_even_index];
}



