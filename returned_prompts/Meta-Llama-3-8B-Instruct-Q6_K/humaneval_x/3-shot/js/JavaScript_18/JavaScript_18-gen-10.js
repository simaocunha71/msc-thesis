  let count = 0;
  let position = 0;
  
  while (true) {
    position = string.indexOf(substring, position);
    if (position === -1) {
      break;
    }
    count++;
    position += substring.length;
  }
  
  return count;
}