  var smallest_even_value = Infinity;
  var smallest_index = -1;

  for (var i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0 && arr[i] < smallest_even_value) {
      smallest_even_value = arr[i];
      smallest_index = i;
    }
  }

  return smallest_index == -1 ? [] : [smallest_even_value, smallest_index];
}



