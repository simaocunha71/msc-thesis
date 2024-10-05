  var depth = 0;

  for (const c of lst[0]) {
    if (c == '(') {
      depth += 1;
    } else {
      depth -= 1;
    }
  }

  for (const c of lst[1]) {
    if (c == '(') {
      depth += 1;
    } else {
      depth -= 1;
    }
  }

  if (depth == 0) {
    return 'Yes';
  } else {
    return 'No';
  }
}



