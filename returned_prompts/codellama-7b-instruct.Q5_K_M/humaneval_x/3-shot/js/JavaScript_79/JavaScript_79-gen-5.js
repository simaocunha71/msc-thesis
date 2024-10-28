  var result = '';
  for (var i = 0; i < 10; i++) {
    if (decimal - 2 ** i >= 0) {
      result = '1' + result;
      decimal = decimal - 2 ** i;
    } else {
      result = '0' + result;
    }
  }
  return 'db' + result + 'db';
}



