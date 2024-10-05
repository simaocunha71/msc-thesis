  if (arr.length === 0) {
    return [];
  } else {
    let smallest_even_value = Infinity;
    let smallest_index = Infinity;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] % 2 === 0) {
        if (arr[i] < smallest_even_value) {
          smallest_even_value = arr[i];
          smallest_index = i;
        }
      }
    }
    return [smallest_even_value, smallest_index];
  }
}



