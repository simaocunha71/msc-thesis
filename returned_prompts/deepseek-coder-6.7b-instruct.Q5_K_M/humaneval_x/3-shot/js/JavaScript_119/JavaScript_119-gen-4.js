  let s1 = lst[0] + lst[1];
  let s2 = lst[1] + lst[0];
  let stack = [];

  for (let str of [s1, s2]) {
    for (let ch of str) {
      if (ch === '(') {
        stack.push(ch);
      } else if (ch === ')' && stack.length > 0 && stack[stack.length - 1] === '(') {
        stack.pop();
      } else {
        return 'No';
      }
    }
    if (stack.length !== 0) {
      stack = [];
    } else {
      return 'Yes';
    }
  }

  return 'No';
}



