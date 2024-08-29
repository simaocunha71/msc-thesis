  let result = true;
  const stack = [];

  for (const c of string) {
    if (c == '[') {
      stack.push(c);
    } else if (c == ']') {
      if (stack.length == 0) {
        result = false;
      } else {
        stack.pop();
      }
    }
  }

  return result;
}



