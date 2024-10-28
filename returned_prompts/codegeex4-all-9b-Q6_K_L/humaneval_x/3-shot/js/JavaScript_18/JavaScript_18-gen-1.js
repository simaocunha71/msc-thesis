  let count = 0;
  let index = 0;
  while (true) {
    index = string.indexOf(substring, index);
    if (index == -1) {
      break;
    } else {
      count += 1;
      index += 1;
    }
  }
  return count;
}



