  var open_parens = 0;
  var closed_parens = 0;

  for (const c of lst[0]) {
    if (c == '(') {
      open_parens += 1;
    } else {
      closed_parens += 1;
    }
  }

  for (const c of lst[1]) {
    if (c == '(') {
      open_parens += 1;
    } else {
      closed_parens += 1;
    }
  }

  if (open_parens == closed_parens) {
    return 'Yes';
  } else {
    return 'No';
  }
}



