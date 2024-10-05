  var first_string = lst[0];
  var second_string = lst[1];
  var first_depth = 0;
  var second_depth = 0;

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

  if (first_depth == 0 && second_depth == 0) {
    return 'Yes';
  } else if (first_depth != 0 && second_depth == 0) {
    return 'No';
  } else if (first_depth == 0 && second_depth != 0) {
    return 'No';
  } else {
    return 'Yes';
  }
}