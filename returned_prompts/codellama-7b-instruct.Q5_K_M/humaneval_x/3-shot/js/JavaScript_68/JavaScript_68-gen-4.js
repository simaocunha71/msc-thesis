  if (arr.length == 0) return [];
  var min_value = Infinity;
  var min_index = 0;
  var is_even = false;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) {
      if (arr[i] < min_value) {
        min_value = arr[i];
        min_index = i;
        is_even = true;
      }
    }
  }
  if (!is_even) return [];
  return [min_value, min_index];
}



