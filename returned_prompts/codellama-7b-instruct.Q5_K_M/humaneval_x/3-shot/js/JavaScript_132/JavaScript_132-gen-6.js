  const brackets = ['[', ']'];
  const stack = [];

  for (const c of string) {
    if (brackets.includes(c)) {
      if (c == '[') {
        stack.push(c);
      } else {
        if (stack.length > 0) {
          const top = stack.pop();
          if (top == '[') {
            return true;
          }
        }
      }
    }
  }

  return false;
}



