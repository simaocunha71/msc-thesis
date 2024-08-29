  let open = 0;
  for (let i = 0; i < lst[0].length; i++) {
    if (lst[0][i] == '(') {
      open += 1;
    } else {
      open -= 1;
    }
    if (open < 0) {
      return 'No';
    }
  }
  open = 0;
  for (let i = 0; i < lst[1].length; i++) {
    if (lst[1][i] == '(') {
      open += 1;
    } else {
      open -= 1;
    }
    if (open < 0) {
      return 'No';
    }
  }
  if (open != 0) {
    return 'No';
  }
  return 'Yes';
}



