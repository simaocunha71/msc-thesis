  let result = "";
  for (const c of string) {
    if (c == c.toLowerCase()) {
      result += c.toUpperCase();
    } else {
      result += c.toLowerCase();
    }
  }
  return result;
}



