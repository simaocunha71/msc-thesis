  var left_to_right_distance = 0;
  var right_to_left_distance = 0;
  var count = 0;

  for (let i = 0; i < n; i++) {
    left_to_right_distance += i;
    right_to_left_distance += n - i - 1;
  }

  while (left_to_right_distance < right_to_left_distance) {
    left_to_right_distance += 1;
    right_to_left_distance -= 1;
    count += 1;
  }

  return count;
}



