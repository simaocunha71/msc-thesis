  let left_paren = 0;
  let right_paren = 0;

  for (const c of lst[0]) {
    if (c == '(') {
      left_paren += 1;
    } else if (c == ')') {
      right_paren += 1;
    }
  }

  for (const c of lst[1]) {
    if (c == '(') {
      left_paren += 1;
    } else if (c == ')') {
      right_paren += 1;
    }
  }

  if (left_paren == right_paren) {
    return 'Yes';
  } else {
    return 'No';
  }
}



