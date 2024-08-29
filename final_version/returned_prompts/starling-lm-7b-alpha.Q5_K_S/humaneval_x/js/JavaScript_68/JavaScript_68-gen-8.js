  let even_index = -1;
  let min_even = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0 && arr[i] < min_even) {
      min_even = arr[i];
      even_index = i;
    }
  }

  return even_index != -1 ? [min_even, even_index] : [];
}



