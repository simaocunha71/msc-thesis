  let depth = 0;

  for (const bracket of brackets) {
    if (bracket == '(') {
      depth += 1;
    } else if (bracket == ')') {
      depth -= 1;
    }

    if (depth < 0) {
      return false;
    }
  }

  return depth == 0;
}



