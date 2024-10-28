  var total = 0;

  for (const s of lst) {
    for (const c of s) {
      if (c == '(') {
        total += 1;
      } else {
        total -= 1;
      }
    }
  }

  if (total == 0) {
    return 'Yes';
  } else {
    return 'No';
  }
}