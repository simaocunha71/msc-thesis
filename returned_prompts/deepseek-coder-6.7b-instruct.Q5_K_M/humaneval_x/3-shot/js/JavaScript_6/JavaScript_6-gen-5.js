  return paren_string.split(' ').map(paren_group => {
    let maxDepth = 0;
    let currentDepth = 0;

    for (const char of paren_group) {
      if (char === '(') {
        currentDepth += 1;
        if (currentDepth > maxDepth) {
          maxDepth = currentDepth;
        }
      } else if (char === ')') {
        currentDepth -= 1;
      }
    }

    return maxDepth;
  });
}



