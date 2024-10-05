  let smallest_even = null;
  let smallest_even_index = null;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) {
      if (smallest_even == null || arr[i] < smallest_even) {
        smallest_even = arr[i];
        smallest_even_index = i;
      }
    }
  }

  if (smallest_even == null) {
    return [];
  } else {
    return [smallest_even, smallest_even_index];
  }
}