  var closest_pair = [];
  var closest_distance = 10000000000000000000000000.0;

  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j) {
        let distance = Math.abs(numbers[i] - numbers[j]);
        if (distance < closest_distance) {
          closest_distance = distance;
          closest_pair[0] = numbers[i];
          closest_pair[1] = numbers[j];
        }
      }
    }
  }
  return closest_pair;
}



