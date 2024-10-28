  var result = 'db';

  while (decimal > 0) {
    result = String(decimal % 2) + result;
    decimal = Math.floor(decimal / 2);
  }

  return result + 'db';
}



