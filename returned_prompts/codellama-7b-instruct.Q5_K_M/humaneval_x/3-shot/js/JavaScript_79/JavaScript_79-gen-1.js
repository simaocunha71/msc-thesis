  var binary_string = '';

  while (decimal > 0) {
    if (decimal % 2 == 0) {
      binary_string = '0' + binary_string;
    } else {
      binary_string = '1' + binary_string;
    }

    decimal = Math.floor(decimal / 2);
  }

  return 'db' + binary_string + 'db';
}



