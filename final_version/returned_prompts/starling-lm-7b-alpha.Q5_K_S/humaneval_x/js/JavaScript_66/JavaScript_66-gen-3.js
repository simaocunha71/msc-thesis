  let result = 0;
  for (const c of s) {
    if (c === c.toUpperCase()) {
      result += c.charCodeAt(0);
    }
  }
  return result;
}



