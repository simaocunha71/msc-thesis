  let count = 0;
  let position = string.indexOf(substring);

  while (position != -1) {
    count++;
    position = string.indexOf(substring, position + 1);
  }

  return count;
}



