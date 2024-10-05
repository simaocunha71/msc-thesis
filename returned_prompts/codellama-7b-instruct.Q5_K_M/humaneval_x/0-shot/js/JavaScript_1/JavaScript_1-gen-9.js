const separateParenGroups = (paren_string) => {
  // Find the first open paren and ignore any spaces before it
  let start_index = paren_string.indexOf('(');
  while (start_index > 0 && paren_string[start_index - 1] === ' ') {
    start_index--;
  }

  // Find the first closed paren, skipping over any nested groups
  let end_index = paren_string.indexOf(')');
  let balance = 0;
  let last_end_index = end_index;
  while (end_index > start_index) {
    balance++;
    end_index = paren_string.indexOf(')', end_index + 1);
    if (end_index === -1) {
      throw new Error('Unmatched paren');
    }
    while (balance !== 0) {
      if (paren_string[end_index - 1] === '(') {
        balance--;
      } else if (paren_string[end_index - 1] === ')') {
        balance++;
      }
      end_index = paren_string.indexOf(')', end_index + 1);
      if (end_index === -1) {
        throw new Error('Unmatched paren');
      }
    }
    if (end_index < last_end_index) {
      throw new Error('Unmatched paren');
    }
    last_end_index = end_index;
  }

  // Separate the groups
  let groups = [];
  let group_start = 0;
  let group_end = end_index + 1;
  while (group_start < paren_string.length) {
    groups.push(paren_string.substring(group_start, group_end));
    group_start = group_end;
    group_end = paren_string.indexOf('(', group_end);
    if (group_end === -1) {
      throw new Error('Unmatched paren');
    }
    while (paren_string[group_end - 1]