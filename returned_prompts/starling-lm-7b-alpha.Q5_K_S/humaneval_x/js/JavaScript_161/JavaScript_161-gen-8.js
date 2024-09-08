  let result = '';
  for (const c of s) {
    if (c >= 'a' && c <= 'z') {
      result += String.fromCharCode(c.charCodeAt(0) - 32);
    } else if (c >= 'A' && c <= 'Z') {
      result += String.fromCharCode(c.charCodeAt(0) + 32);
    } else {
      result += c;
    }
  }
  return result.split('').reverse().join('');
}



