  let open = 0;
  let close = 0;

  for (let c of lst[0]) {
    if (c == '(') {
      open++;
    } else {
      if (open == 0) {
        return 'No';
      }
      open--;
    }
  }

  for (let c of lst[1]) {
    if (c == '(') {
      close++;
    } else {
      if (close == 0) {
        return 'No';
      }
      close--;
    }
  }

  if (open != close) {
    return 'No';
  }

  return 'Yes';
}