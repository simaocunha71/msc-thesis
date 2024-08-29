  var counter = 0;
  for (var i = 0; i < string.length; i++) {
    if (string.substring(i, i + substring.length) == substring) {
      counter += 1;
    }
  }
  return counter;
}



