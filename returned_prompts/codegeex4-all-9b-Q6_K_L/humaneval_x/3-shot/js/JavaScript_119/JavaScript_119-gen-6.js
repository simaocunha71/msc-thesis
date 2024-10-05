  let result = false;
  const arr = lst[0] + lst[1];
  let depth = 0;
  for (const c of arr) {
    if (c == '(') {
      depth += 1;
    } else if (c == ')') {
      depth -= 1;
    }
    if (depth < 0) {
      return 'No';
    }
  }
  if (depth == 0) {
    result = true;
  }
  return result ? 'Yes' : 'No';
}