  let left = 0;
  let right = 0;

  for (const c of lst[0]) {
    if (c == '(') {
      left += 1;
    } else {
      left -= 1;
    }
  }

  for (const c of lst[1]) {
    if (c == ')') {
      right += 1;
    } else {
      right -= 1;
    }
  }

  return left == 0 && right == 0 ? 'Yes' : 'No';
}



