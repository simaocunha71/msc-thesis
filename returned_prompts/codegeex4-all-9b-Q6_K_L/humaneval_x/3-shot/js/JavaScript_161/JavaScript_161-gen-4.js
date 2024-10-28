  var result = '';
  var lower = 'abcdefghijklmnopqrstuvwxyz';
  var upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

  for (const c of s) {
    if (lower.includes(c)) {
      result += c.toUpperCase();
    } else if (upper.includes(c)) {
      result += c.toLowerCase();
    } else {
      result += c;
    }
  }

  return result;
}