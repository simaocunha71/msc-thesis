  const nested_parens = paren_string.split(' ');
  const results = [];

  for (let i = 0; i < nested_parens.length; i++) {
    let level = 0;

    for (let j = 0; j < nested_parens[i].length; j++) {
      if (nested_parens[i][j] === '(') {
        level++;
      } else if (nested_parens[i][j] === ')') {
        level--;
      }
    }

    results.push(level);
  }

  return results;
}
