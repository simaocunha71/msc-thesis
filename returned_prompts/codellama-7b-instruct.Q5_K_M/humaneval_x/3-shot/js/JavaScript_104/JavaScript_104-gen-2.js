  var result = [];
  var digits = [];

  for (var i = 0; i < x.length; i++) {
    digits = x[i].toString().split('');
    for (var j = 0; j < digits.length; j++) {
      if (digits[j] % 2 == 1) {
        result.push(x[i]);
        break;
      }
    }
  }

  return result.sort((a, b) => a - b);
}



