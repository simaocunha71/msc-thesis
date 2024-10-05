  var smallest_even = 10000;
  var smallest_index = -1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) {
      if (arr[i] < smallest_even) {
        smallest_even = arr[i];
        smallest_index = i;
      } else if (arr[i] == smallest_even) {
        if (i < smallest_index) {
          smallest_index = i;
        }
      }
    }
  }

  if (smallest_even == 10000) {
    return [];
  } else {
    return [smallest_even, smallest_index];
  }
}



