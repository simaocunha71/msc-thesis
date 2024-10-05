let stack = [];
  let group = [];
  let groups = [];

  for (let i = 0; i < paren_string.length; i++) {
    if (paren_string[i] === '(') {
      stack.push(paren_string[i]);
      group.push(paren_string[i]);
    } else if (paren_string[i] === ')') {
      stack.pop();
      group.push(paren_string[i]);
      if (stack.length === 0) {
        groups.push(group.join(''));
        group = [];
      }
    }
  }

  return groups;
};


console.log(separateParenGroups('(  )  (( ))  (( )( ))')) // ['()', '(())', '((()))']

This code works by iterating over the input string, and keeping track of the balance of the parentheses with a stack. When it encounters