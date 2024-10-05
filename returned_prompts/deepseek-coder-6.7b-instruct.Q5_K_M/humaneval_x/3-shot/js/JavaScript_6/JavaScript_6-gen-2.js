  return paren_string.split(' ').map(group => {
    let count = 0;
    let max = 0;
    for (const char of group) {
      if (char === '(') {
        count++;
        if (count > max) {
          max = count;
        }
      } else if (char === ')') {
        count--;
      }
    }
    return max;
  });
}



