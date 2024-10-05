  var count = 0;
  var idx = string.indexOf(substring);
  while (idx != -1) {
    count += 1;
    idx = string.indexOf(substring, idx + 1);
  }
  return count;
}



