  let result = '';
  for (const c of string) {
    result += (c >= 'a' && c <= 'z') ? c.toUpperCase() : c.toLowerCase();
  }
  return result;
}



