  let open = 0;
  let close = 0;

  for (const c of lst[0]) {
    if (c == '(') {
      open++;
    } else {
      close++;
    }
  }

  for (const c of lst[1]) {
    if (c == '(') {
      open++;
    } else {
      close++;
    }
  }

  if (open == close) {
    return 'Yes';
  } else {
    return 'No';
  }
}