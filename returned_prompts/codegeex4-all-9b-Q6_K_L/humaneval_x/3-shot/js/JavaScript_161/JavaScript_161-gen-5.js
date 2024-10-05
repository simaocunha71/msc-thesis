  var result = '';

  for (const c of s) {
    if ('a' <= c && c <= 'z') {
      result += c.toUpperCase();
    } else if ('A' <= c && c <= 'Z') {
      result += c.toLowerCase();
    } else {
      result += c;
    }
  }

  return result.split('').reverse().join('');
}