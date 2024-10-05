  let open = 0;
  let close = 0;

  for (const c of lst[0]) {
    if (c == '(') {
      open++;
    } else {
      close++;
    }
  }

  if (open != close) {
    return 'No';
  }

  open = 0;
  close = 0;

  for (const c of lst[1]) {
    if (c == '(') {
      open++;
    } else {
      close++;
    }
  }

  if (open != close) {
    return 'No';
  }

  if (open > 0) {
    return 'No';
  }

  return 'Yes';
}
// or
const matchParens = (lst) => {
  let open = 0;
  let close = 0;

  for (const c of lst[0] + lst[1]) {
    if (c == '(') {
      open++;
    } else {
      close++;
      if (open == 0) {
        return 'No';
      }
      open--;
    }
  }

  return 'Yes';
}