  if (arr.length <= 1) {
    return true;
  }

  let max_index = 0;
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
      max_index = i;
    }
  }

  for (let i = 0; i < arr.length; i++) {
    if (max_index < i) {
      return false;
    }
    max_index = (max_index + 1) % arr.length;
  }

  return true;
}



