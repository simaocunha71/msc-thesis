  let count = 0;
  let idx = string.indexOf(substring);
  while (idx != -1) {
    count += 1;
    idx = string.indexOf(substring, idx + 1);
  }
  return count;
}



