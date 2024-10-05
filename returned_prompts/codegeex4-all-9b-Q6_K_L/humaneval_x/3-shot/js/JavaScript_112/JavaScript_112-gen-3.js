  var result = s.split('').filter(e => !c.includes(e)).join('');
  var check = result.split('').reverse().join('');
  return [result, result == check];
}