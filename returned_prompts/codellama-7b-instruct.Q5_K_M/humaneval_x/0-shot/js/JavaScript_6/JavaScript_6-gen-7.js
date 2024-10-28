const parseNestedParens = (paren_string) => {
  const paren_groups = paren_string.split(' ');
  return paren_groups.map((paren_group) => {
    const open_parens = paren_group.split('').filter(char => char === '(').length;
    const close_parens = paren_group.split('').filter(char => char === ')').length;
    return Math.max(open_parens, close_parens);
  });
};

