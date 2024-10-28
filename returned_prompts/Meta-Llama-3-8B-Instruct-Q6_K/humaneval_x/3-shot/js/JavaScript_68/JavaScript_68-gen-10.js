  let min_even = Infinity;
  let min_even_index = -1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < min_even) {
      min_even = arr[i];
      min_even_index = i;
    }
  }

  if (min_even === Infinity) {
    return [];
  }

  return [min_even, min_even_index];
}