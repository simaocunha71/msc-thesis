  var result = '';

  for (const c of s) {
    if (c == c.toUpperCase()) {
      result += c.toLowerCase();
    } else if (c == c.toLowerCase()) {
      result += c.toUpperCase();
    } else {
      result += c;
    }
  }

  return result;
}