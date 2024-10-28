  return paren_string.split(' ').map(str => {
    let maxDepth = 0, currentDepth = 0;
    for (let char of str) {
      if (char === '(') {
        currentDepth++;
        if (currentDepth > maxDepth) {
          maxDepth = currentDepth;
        }
      } else if (char === ')') {
        currentDepth--;
      }
    }
    return maxDepth;
  });
}



