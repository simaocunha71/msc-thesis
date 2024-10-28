  var count = 0;
  var index = string.indexOf(substring);
  while (index != -1) {
    count += 1;
    index = string.indexOf(substring, index + 1);
  }

  return count;
}



