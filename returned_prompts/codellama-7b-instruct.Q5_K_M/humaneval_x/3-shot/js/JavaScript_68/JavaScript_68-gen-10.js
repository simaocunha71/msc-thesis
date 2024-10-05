  if (arr.length === 0) {
    return [];
  }

  var smallest_value = Infinity;
  var smallest_index = -1;

  for (var i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < smallest_value) {
      smallest_value = arr[i];
      smallest_index = i;
    }
  }

  return [smallest_value, smallest_index];
}



