  var result = '';
  for (const i of s) {
    if (!c.includes(i)) {
      result += i;
    }
  }

  var reversed = result.split('').reverse().join('');
  return [result, result == reversed];
}



