const parseNestedParens = (paren_string) => {
  const groups = paren_string.split(' ');
  return groups.map(group => {
    const open_parens = [];
    for (let i = 0; i < group.length; i++) {
      if (group[i] === '(') open_parens.push(i);
      if (group[i] === ')') open_parens.pop();
    }
    return open_parens.length;
  });
};
