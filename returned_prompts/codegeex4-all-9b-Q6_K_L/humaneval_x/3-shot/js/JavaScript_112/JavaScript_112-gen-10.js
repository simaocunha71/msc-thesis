  var result = '';
  var c_set = new Set(c);

  for (const c of s) {
    if (!c_set.has(c)) {
      result += c;
    }
  }

  return [result, result == result.split('').reverse().join('')];
}