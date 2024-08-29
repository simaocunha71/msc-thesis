  let result = "";
  for (const c of s) {
    if (c >= 'a' && c <= 'z') {
      result += String.fromCharCode((c.charCodeAt(0) - 97 + 2 * 2) % 26 + 97);
    } else if (c >= 'A' && c <= 'Z') {
      result += String.fromCharCode((c.charCodeAt(0) - 65 + 2 * 2) % 26 + 65);
    } else {
      result += c;
    }
  }
  return result;
}



