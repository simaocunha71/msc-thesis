  var result = [];
  var check = false;

  for (let i = 0; i < s.length; i++) {
    if (c.indexOf(s[i]) == -1) {
      result.push(s[i]);
    }
  }

  if (result.join('') == result.join('').split('').reverse().join('')) {
    check = true;
  }

  return [result.join(''), check];
}



