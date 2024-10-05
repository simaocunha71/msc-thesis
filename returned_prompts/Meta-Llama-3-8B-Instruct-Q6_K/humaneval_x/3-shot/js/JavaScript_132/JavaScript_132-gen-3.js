  let count = 0;
  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      count++;
    } else if (string[i] === ']') {
      if (count > 0) {
        count--;
      } else {
        return false;
      }
    }
  }
  return count > 0;
}