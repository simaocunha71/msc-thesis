  var result = s.replace(new RegExp('[' + c + ']', 'g'), '');
  var reversed = result.split('').reverse().join('');

  return [result, result == reversed];
}