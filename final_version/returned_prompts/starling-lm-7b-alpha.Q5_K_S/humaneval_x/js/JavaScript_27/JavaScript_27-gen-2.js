  let result = '';
  for (const c of string) {
    if (c >= 'a' && c <= 'z') {
      result += c.toUpperCase();
    } else if (c >= 'A' && c <= 'Z') {
      result += c.toLowerCase();
    } else {
      result += c;
    }
  }
  return result;
}



