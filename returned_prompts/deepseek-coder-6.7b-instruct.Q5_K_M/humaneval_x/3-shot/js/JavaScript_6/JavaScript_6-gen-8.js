  return paren_string.split(' ').map(group => {
    let maxDepth = 0;
    let currentDepth = 0;

    for (let char of group) {
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



