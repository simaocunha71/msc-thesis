const separateParenGroups = (paren_string) => {
  const paren_groups = [];
  let current_group = '';
  let current_paren_count = 0;
  for (let char of paren_string) {
    if (char === '(') {
      current_paren_count += 1;
      current_group += char;
    } else if (char === ')') {
      current_paren_count -= 1;
      current_group += char;
      if (current_paren_count === 0) {
        paren_groups.push(current_group);
        current_group = '';
      }
    } else {
      current_group += char;
    }
  }
  return paren_groups;
};
