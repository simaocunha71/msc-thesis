  var result = '';
  for (const c of s) {
    if (c >= 'a' && c <= 'z') {
      result += c.toUpperCase();
    } else if (c >= 'A' && c <= 'Z') {
      result += c.toLowerCase();
    } else {
      result += c;
    }
  }

  if (result.match(/[a-zA-Z]/g) === null) {
    return result.split('').reverse().join('');
  }

  return result;
}