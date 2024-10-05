  var opening_brackets = 0;
  var closing_brackets = 0;

  for (const bracket of brackets) {
    if (bracket == '<') {
      opening_brackets += 1;
    } else if (bracket == '>') {
      closing_brackets += 1;
    }
  }

  if (opening_brackets == closing_brackets) {
    return true;
  } else {
    return false;
  }
}



