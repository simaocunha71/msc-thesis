const separateParenGroups = (paren_string) => {
  const open_brackets = [];
  const close_brackets = [];
  const groups = [];
  for (let i = 0; i < paren_string.length; i++) {
    const bracket = paren_string[i];
    if (bracket === '(') {
      open_brackets.push(i);
    } else if (bracket === ')') {
      if (open_brackets.length > 0) {
        const start_index = open_brackets.pop();
        close_brackets.push(i);
        groups.push(paren_string.substring(start_index, i + 1));
      } else {
        console.log('Invalid input.');
      }
    }
  }
  if (open_brackets.length > 0) {
    console.log('Invalid input.');
  }
  return groups;
}


