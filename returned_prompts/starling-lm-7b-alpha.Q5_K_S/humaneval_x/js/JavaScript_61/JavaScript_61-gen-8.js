  let result = true;
  let depth = 0;
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] == '(') {
      depth += 1;
    } else if (brackets[i] == ')') {
      depth -= 1;
    }
    if (depth < 0) {
      result = false;
    }
  }

  return result && depth == 0;
}



