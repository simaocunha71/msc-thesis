  let count = 0;
  let position = 0;

  while  ((position = string.indexOf(substring, position)) != -1)  {
    count++;
    position++;
  }

  return count;
}



