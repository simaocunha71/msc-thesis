  var newString = '';
  for (let c of string) {
    if (c == c.toUpperCase()) {
      newString += c.toLowerCase();
    } else {
      newString += c.toUpperCase();
    }
  }
  return newString;
}



