  var count = 0;
  var start = 0;
  while (start < string.length) {
    var index = string.indexOf(substring, start);
    if (index == -1) {
      break;
    }
    count += 1;
    start = index + 1;
  }
  return count;
}



