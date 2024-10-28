  var result = s;
  var check = false;

  for (var i = 0; i < c.length; i++) {
    var regex = new RegExp(c[i], 'g');
    result = result.replace(regex, '');
  }

  if (result == result.split('').reverse().join('')) {
    check = true;
  }

  return [result, check];
}



