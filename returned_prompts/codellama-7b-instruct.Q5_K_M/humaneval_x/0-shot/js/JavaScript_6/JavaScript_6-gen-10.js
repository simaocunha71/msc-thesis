const parseNestedParens = (paren_string) => {
  const result = [];
  let current_level = 0;
  let current_parens = '';
  for (const paren of paren_string) {
    if (paren === '(') {
      current_level++;
      current_parens += paren;
    } else if (paren === ')') {
      current_level--;
      current_parens += paren;
    } else if (paren === ' ') {
      if (current_level > 0) {
        result.push(current_level);
        current_level = 0;
        current_parens = '';
      }
    } else {
      current_parens += paren;
    }
  }
  if (current_level > 0) result.push(current_level);
  return result;
};

