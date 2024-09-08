  let left_count = 0;

  for (let i = 0; i < lst[0].length; i++) {
    if (lst[0][i] == '(') {
      left_count += 1;
    } else {
      left_count -= 1;
    }
    if (left_count < 0) {
      return 'No';
    }
  }

  if (left_count != 0) {
    return 'No';
  }

  left_count = 0;

  for (let i = 0; i < lst[1].length; i++) {
    if (lst[1][i] == ')') {
      left_count += 1;
    } else {
      left_count -= 1;
    }
    if (left_count < 0) {
      return 'No';
    }
  }

  if (left_count != 0) {
    return 'No';
  }

  return 'Yes';
}



