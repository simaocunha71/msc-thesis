  let result = [];
  let min_even = Infinity;
  let min_index = Infinity;

  for (let i = 0; i < arr.length; i++) {
    let value = arr[i];
    if (value % 2 == 0 && value < min_even) {
      min_even = value;
      min_index = i;
    }
  }

  if (min_even == Infinity) {
    return [];
  } else {
    result.push(min_even);
    result.push(min_index);
    return result;
  }
}