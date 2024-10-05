  return paren_string.split(' ').map(str => {
    let count = 0;
    let max = 0;
    for (let i = 0; i < str.length; i++) {
      if (str[i] === '(') {
        count++;
        if (count > max) {
          max = count;
        }
      } else if (str[i] === ')') {
        count--;
      }
    }
    return max;
  });
}



