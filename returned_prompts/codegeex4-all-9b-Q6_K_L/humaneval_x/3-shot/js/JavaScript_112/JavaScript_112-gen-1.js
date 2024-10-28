  let result = '';
  for (let i = 0; i < s.length; i++) {
    if (!c.includes(s[i])) {
      result += s[i];
    }
  }
  return [result, result == result.split('').reverse().join('')];
}


