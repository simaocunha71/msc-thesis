  let result = 0;
  for (const c of s) {
    if (c >= 'A' && c <= 'Z') {
      result += c.charCodeAt(0) - 64;
    }
  }
  return result;
}



