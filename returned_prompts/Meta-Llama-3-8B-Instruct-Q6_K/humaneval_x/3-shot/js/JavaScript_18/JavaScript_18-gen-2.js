  let count = 0;
  let pos = 0;
  while ((pos = string.indexOf(substring, pos)) != -1) {
    count++;
    pos += substring.length;
  }
  return count;
}