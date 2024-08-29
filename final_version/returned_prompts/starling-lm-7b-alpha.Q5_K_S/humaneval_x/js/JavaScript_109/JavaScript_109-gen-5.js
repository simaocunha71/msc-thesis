  let min_index;
  let temp;
  for (let i = 0; i < arr.length; i++) {
    min_index = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[min_index]) {
        min_index = j;
      }
    }
    if (min_index != i) {
      temp = arr[i];
      arr[i] = arr[min_index];
      arr[min_index] = temp;
    }
  }

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      return false;
    }
  }
  return true;
}



