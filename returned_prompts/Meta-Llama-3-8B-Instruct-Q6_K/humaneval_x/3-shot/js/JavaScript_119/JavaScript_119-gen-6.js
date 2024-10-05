  let stack = [];
  let result = 'Yes';

  for (const s of lst) {
    if (s === '(') {
      stack.push(s);
    } else if (s === ')') {
      if (stack.length === 0) {
        result = 'No';
        break;
      }
      stack.pop();
    }
  }

  if (stack.length > 0) {
    result = 'No';
  }

  return result;
}