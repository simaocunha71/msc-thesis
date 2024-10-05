  var result = s.split('');
  for (const c1 of c) {
    result = result.filter(c2 => c1 != c2);
  }
  var result_string = result.join('');
  return [result_string, result_string == result_string.split('').reverse().join('')];
}