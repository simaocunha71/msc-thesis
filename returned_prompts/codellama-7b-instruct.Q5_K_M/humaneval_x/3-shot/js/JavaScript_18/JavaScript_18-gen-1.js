  let count = 0;
  let i = 0;
  while (true) {
    i = string.indexOf(substring, i);
    if (i == -1) break;
    count++;
    i++;
  }
  return count;
}



