  var count = 0;
  var position = 0;
  while (true) {
    position = string.indexOf(substring, position);
    if (position == -1) break;
    count++;
    position++;
  }
  return count;
}



