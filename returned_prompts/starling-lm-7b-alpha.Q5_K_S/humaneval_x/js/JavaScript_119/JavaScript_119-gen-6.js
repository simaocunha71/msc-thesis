  const balance = (s) => {
    let depth = 0;
    for (const c of s) {
      if (c == '(') {
        depth += 1;
      } else if (c == ')') {
        depth -= 1;
      }
      if (depth < 0) {
        return false;
      }
    }
    return depth == 0;
  };

  return balance(lst[0]) && balance(lst[1]);
}


