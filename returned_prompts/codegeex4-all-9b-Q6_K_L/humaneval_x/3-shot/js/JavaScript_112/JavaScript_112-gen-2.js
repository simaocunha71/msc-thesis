  var result = s.split('').filter(x => !c.includes(x)).join('');
  return [result, result == result.split('').reverse().join('')];
}