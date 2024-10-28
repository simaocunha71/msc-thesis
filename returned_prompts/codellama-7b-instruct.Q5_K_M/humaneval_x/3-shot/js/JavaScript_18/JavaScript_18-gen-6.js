  if (string.indexOf(substring) < 0) {
    return 0;
  }

  var count = 0;
  var index = string.indexOf(substring);

  while (index >= 0) {
    count += 1;
    index = string.indexOf(substring, index + 1);
  }

  return count;
}



