  var collisions = 0;
  var left_to_right = [];
  var right_to_left = [];
  var left_to_right_speed = 1.0 / n;
  var right_to_left_speed = -1.0 / n;

  for (let i = 0; i < n; i++) {
    left_to_right.push(i * left_to_right_speed);
    right_to_left.unshift(i * right_to_left_speed);
  }

  var left_to_right_end = left_to_right[0];
  var right_to_left_end = right_to_left[0];

  while (left_to_right_end != 0 || right_to_left_end != 0) {
    if (left_to_right_end == right_to_left_end) {
      left_to_right.shift();
      right_to_left.shift();
    } else if (left_to_right_end < right_to_left_end) {
      left_to_right_end += left_to_right_speed;
      left_to_right.shift();
    } else {
      right_to_left_end += right_to_left_speed;
      right_to_left.shift();
      collisions += 1;
    }
  }

  return collisions;
}



