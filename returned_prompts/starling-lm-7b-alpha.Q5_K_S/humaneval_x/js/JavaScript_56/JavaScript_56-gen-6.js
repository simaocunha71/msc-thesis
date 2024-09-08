  var counter = 0;
  for (var i = 0; i < brackets.length; i++) {
    if (brackets[i] == '<') {
      counter += 1;
    } else {
      counter -= 1;
    }
    if (counter < 0) {
      return false;
    }
  }
  return counter == 0;
}



