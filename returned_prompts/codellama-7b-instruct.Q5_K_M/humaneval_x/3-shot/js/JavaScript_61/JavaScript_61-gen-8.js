  var opening_brackets = 0;

  for (const b of brackets) {
    if (b == '(') {
      opening_brackets += 1;
    } else if (b == ')') {
      opening_brackets -= 1;
    }
  }

  return opening_brackets == 0;
}



