  var smallest_even = Infinity;
  var smallest_index = -1;
  var smallest_value = Infinity;

  for (var i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0 && arr[i] < smallest_even) {
      smallest_even = arr[i];
      smallest_index = i;
      smallest_value = arr[i];
    } else if (arr[i] % 2 == 0 && arr[i] < smallest_value) {
      smallest_value = arr[i];
      smallest_index = i;
    }
  }

  if (smallest_index >= 0) {
    return [smallest_value, smallest_index];
  } else {
    return [];
  }
}



