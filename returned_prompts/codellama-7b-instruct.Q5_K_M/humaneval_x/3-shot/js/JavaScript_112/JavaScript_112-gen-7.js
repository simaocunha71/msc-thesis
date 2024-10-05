  var result = [];

  for (const char of s) {
    if (c.indexOf(char) == -1) {
      result.push(char);
    }
  }

  return [result.join(''), result.join('').split('').reverse().join('') == result.join('')];
}



