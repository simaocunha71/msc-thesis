  let result = '';

  for (const c of string) {
    if (c == c.toUpperCase()) {
      result += c.toLowerCase();
    } else {
      result += c.toUpperCase();
    }
  }

  return result;
}



