  var count = 0;
  var pos = 0;
  while (true) {
    pos = string.indexOf(substring, pos);
    if (pos == -1) break;
    count += 1;
    pos += 1;
  }
  return count;
}



