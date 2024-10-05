  let open = 0;
  let close = 0;

  for (const c of lst[0]) {
    if (c == '(') {
      open += 1;
    } else {
      close += 1;
    }
  }

  for (const c of lst[1]) {
    if (c == '(') {
      open -= 1;
    } else {
      close -= 1;
    }
  }

  if (open == 0 && close == 0) {
    return 'Yes';
  } else {
    return 'No';
  }
}