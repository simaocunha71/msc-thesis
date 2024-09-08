  let result = '';
  for (const c of string) {
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



