  const left_to_right = n;
  const right_to_left = n;
  const total_distance = 1000000000;
  const initial_distance = 100000000;

  const left_to_right_distance = initial_distance + total_distance * (left_to_right - 1) / left_to_right;
  const right_to_left_distance = initial_distance + total_distance * (right_to_left - 1) / right_to_left;

  if (left_to_right_distance >= right_to_left_distance) {
    return n - 1;
  }

  return n;
}



