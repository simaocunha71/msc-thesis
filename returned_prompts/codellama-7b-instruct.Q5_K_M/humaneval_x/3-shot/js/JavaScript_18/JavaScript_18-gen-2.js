  var count = 0;
  var pos = 0;

  while (true) {
    pos = string.indexOf(substring, pos);
    if (pos == -1) {
      break;
    } else {
      count += 1;
      pos += substring.length;
    }
  }

  return count;
}



