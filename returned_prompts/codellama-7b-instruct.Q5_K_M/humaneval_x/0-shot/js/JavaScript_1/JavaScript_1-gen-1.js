
const separateParenGroups = (paren_string) => {
  const groups = [];
  let group = '';

  for (let i = 0; i < paren_string.length; i++) {
    const current = paren_string[i];
    if (current === '(') {
      group += current;
    } else if (current === ')') {
      group += current;
      groups.push(group);
      group = '';
    }
  }
  return groups;
};

