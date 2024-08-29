  let openBrackets = [];
  let count = 0;
  for (const c of brackets) {
    if (c == '<') {
      openBrackets.push(c);
    } else if (c == '>') {
      if (openBrackets.length == 0) {
        return false;
      } else {
        openBrackets.pop();
        count += 1;
      }
    }
  }

  return count == openBrackets.length;
}



