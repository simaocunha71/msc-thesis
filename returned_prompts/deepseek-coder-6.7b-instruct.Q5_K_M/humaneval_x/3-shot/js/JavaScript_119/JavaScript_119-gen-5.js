  let s = lst[0] + lst[1];
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] == '(') {
      stack.push(s[i]);
    } else if (s[i] == ')') {
      if (stack.length == 0) {
        return 'No';
      }
      stack.pop();
    }
  }
  return stack.length == 0 ? 'Yes' : 'No';
}



