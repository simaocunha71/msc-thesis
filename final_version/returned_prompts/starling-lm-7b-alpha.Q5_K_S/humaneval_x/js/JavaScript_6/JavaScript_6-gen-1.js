  const paren_groups = paren_string.split(' ');
  const result = [];

  for (const paren_group of paren_groups) {
    let nesting_level = 0;
    for (const paren of paren_group) {
      if (paren == '(') {
        nesting_level += 1;
      } else if (paren == ')') {
        nesting_level -= 1;
      }
      if (nesting_level > result[result.length - 1]) {
        result.push(nesting_level);
      }
    }
  }

  return result;
}



