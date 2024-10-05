  let open_count = 0;
  let close_count = 0;

  for (let i = 0; i < lst[0].length; i++) {
    if (lst[0][i] == '(') {
      open_count++;
    } else if (lst[0][i] == ')') {
      close_count++;
    }
  }

  for (let i = 0; i < lst[1].length; i++) {
    if (lst[1][i] == '(') {
      open_count++;
    } else if (lst[1][i] == ')') {
      close_count++;
    }
  }

  if (open_count == close_count) {
    return 'Yes';
  } else {
    return 'No';
  }
}