  var smallest = Infinity;
  var smallest_index = -1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0 && arr[i] <= smallest) {
      smallest = arr[i];
      smallest_index = i;
    }
  }

  if (smallest_index == -1) {
    return [];
  } else {
    return [smallest, smallest_index];
  }
}