  let first_string = lst[0];
  let second_string = lst[1];

  let first_depth = 0;
  let second_depth = 0;

  for (const c of first_string) {
    if (c == '(') {
      first_depth += 1;
    } else if (c == ')') {
      first_depth -= 1;
    }
  }

  for (const c of second_string) {
    if (c == '(') {
      second_depth += 1;
    } else if (c == ')') {
      second_depth -= 1;
    }
  }

  let min_depth = Math.min(first_depth, second_depth);
  let max_depth = Math.max(first_depth, second_depth);

  if (max_depth - min_depth <= 2) {
    return 'Yes';
  } else {
    return 'No';
  }
}