  var result = '';
  for (const c of string) {
    if (c.match(/[a-z]/)) {
      result += c.toUpperCase();
    } else {
      result += c.toLowerCase();
    }
  }

  return result;
}



