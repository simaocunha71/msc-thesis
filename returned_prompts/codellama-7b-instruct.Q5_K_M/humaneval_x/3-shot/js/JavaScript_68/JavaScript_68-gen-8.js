  var result = [];
  var smallest_even_value = null;
  var smallest_even_index = null;

  for (var i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) {
      if (smallest_even_value == null) {
        smallest_even_value = arr[i];
        smallest_even_index = i;
      } else if (arr[i] < smallest_even_value) {
        smallest_even_value = arr[i];
        smallest_even_index = i;
      }
    }
  }

  if (smallest_even_value != null) {
    result.push(smallest_even_value);
    result.push(smallest_even_index);
  }

  return result;
}



