  let open = 0;
  let close = 0;
  for (const c of lst[0] + lst[1]) {
    if (c == '(') {
      open++;
    } else {
      close++;
    }
  }
  return (open == close) ? 'Yes' : 'No';
}