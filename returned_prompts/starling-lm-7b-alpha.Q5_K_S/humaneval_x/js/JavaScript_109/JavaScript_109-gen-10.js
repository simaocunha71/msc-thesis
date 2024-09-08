  let max_index = 0;
  let max_value = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max_value) {
      max_value = arr[i];
      max_index = i;
    }
  }

  if (max_index == 0) {
    return true;
  }

  let max_index_original_position = max_index;
  while (max_index_original_position != 0) {
    max_index_original_position = (max_index_original_position + 1) % arr.length;
    let temp = arr[max_index_original_position];
    arr[max_index_original_position] = arr[max_index];
    arr[max_index] = temp;
  }

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[i - 1]) {
      return false;
    }
  }
  return true;
}



