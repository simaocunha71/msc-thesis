  var count = 0;
  var index = 0;

  while (true) {
    index = string.indexOf(substring, index);
    if (index == -1) {
      break;
    }
    count += 1;
    index += 1;
  }

  return count;
}



