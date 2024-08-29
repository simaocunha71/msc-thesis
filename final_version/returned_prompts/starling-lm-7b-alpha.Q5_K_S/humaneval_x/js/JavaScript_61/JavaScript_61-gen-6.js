  var open = 0;

  for (var i = 0; i < brackets.length; i++) {
    if (brackets[i] == '(') {
      open += 1;
    } else {
      open -= 1;
      if (open < 0) {
        return false;
      }
    }
  }

  return open == 0;
}



