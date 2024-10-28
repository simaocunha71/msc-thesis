  var totalParens = 0;

  for (const s of lst) {
    for (const c of s) {
      if (c == '(') {
        totalParens += 1;
      } else if (c == ')') {
        totalParens -= 1;
      }
    }
  }

  return totalParens == 0 ? 'Yes' : 'No';
}