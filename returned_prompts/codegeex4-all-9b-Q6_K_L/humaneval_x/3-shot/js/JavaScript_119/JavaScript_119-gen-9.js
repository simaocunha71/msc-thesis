  var left = 0;
  var right = 0;
  for (const c of lst[0]) {
    if (c == '(') {
      left += 1;
    } else if (c == ')') {
      right += 1;
    }
  }
  for (const c of lst[1]) {
    if (c == '(') {
      left += 1;
    } else if (c == ')') {
      right += 1;
    }
  }
  if (left == right) {
    return 'Yes';
  } else {
    return 'No';
  }
}

