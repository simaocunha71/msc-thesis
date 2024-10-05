  let smallest_distance = Math.abs(numbers[0] - numbers[1]);
  let smallest_index = 0;
  let smallest_index_2 = 1;

  for (let i = 1; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let distance = Math.abs(numbers[i] - numbers[j]);
      if (distance < smallest_distance) {
        smallest_distance = distance;
        smallest_index = i;
        smallest_index_2 = j;
      }
    }
  }

  return [numbers[smallest_index], numbers[smallest_index_2]];
}



