  let result = '';
  for (const char of s) {
    if (c.indexOf(char) == -1) {
      result += char;
    }
  }
  let result_reverse = result.split('').reverse().join('');
  return [result, result_reverse == result];
}



