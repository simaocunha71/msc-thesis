  var count = 0;
  var index = 0;
  while ((index = string.indexOf(substring, index)) > -1) {
    count++;
    index += substring.length;
  }
  return count;
}



