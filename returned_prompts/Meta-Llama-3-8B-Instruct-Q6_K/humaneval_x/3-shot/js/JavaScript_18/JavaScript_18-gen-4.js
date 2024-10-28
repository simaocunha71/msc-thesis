  let count = 0;
  let pos = 0;

  while (true) {
    pos = string.indexOf(substring, pos);
    if (pos == -1) {
      break;
    }
    count++;
    pos += substring.length;
  }

  return count;
}