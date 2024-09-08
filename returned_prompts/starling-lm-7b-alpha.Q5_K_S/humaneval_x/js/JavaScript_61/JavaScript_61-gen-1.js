  var result = true;
  var depth = 0;

  for (const c of brackets) {
    if (c == '(') {
      depth += 1;
    } else if (c == ')') {
      depth -= 1;
    }
    result = result && (depth >= 0);
  }

  return result && (depth == 0);
}



