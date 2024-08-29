  let left_count = 0;
  let right_count = 0;
  for (const c of lst[0]) {
    if (c == '(') {
      left_count += 1;
    } else if (c == ')') {
      left_count -= 1;
      if (left_count < 0) {
        return 'No';
      }
    }
  }
  if (left_count != 0) {
    return 'No';
  }
  for (const c of lst[1]) {
    if (c == '(') {
      right_count += 1;
    } else if (c == ')') {
      right_count -= 1;
      if (right_count < 0) {
        return 'No';
      }
    }
  }
  if (right_count != 0) {
    return 'No';
  }
  return 'Yes';
}



