  var result = '';
  for (const c of string) {
    if (c.match(/[a-z]/)) {
      result += c.toUpperCase();
    } else if (c.match(/[A-Z]/)) {
      result += c.toLowerCase();
    } else {
      result += c;
    }
  }
  return result;
}



