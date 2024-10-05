  return paren_string.split(' ').map(group => {
    var maxDepth = 0;
    var currentDepth = 0;

    for(const char of group) {
      if(char === '(') {
        currentDepth += 1;
        if(currentDepth > maxDepth) {
          maxDepth = currentDepth;
        }
      } else if(char === ')') {
        currentDepth -= 1;
      }
    }

    return maxDepth;
  });
}



