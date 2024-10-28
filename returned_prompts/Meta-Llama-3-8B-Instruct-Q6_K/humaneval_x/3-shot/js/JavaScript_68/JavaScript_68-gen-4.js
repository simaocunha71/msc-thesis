  let smallest_even_value = Infinity;
  let smallest_even_index = -1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < smallest_even_value) {
      smallest_even_value = arr[i];
      smallest_even_index = i;
    }
  }

  if (smallest_even_value === Infinity) {
    return [];
  }

  return [smallest_even_value, smallest_even_index];
}