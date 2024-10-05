  var binary_string = '';
  var remainder = N;

  while (remainder > 0) {
    var current_digit = remainder % 2;
    binary_string = current_digit + binary_string;
    remainder = Math.floor(remainder / 2);
  }

  return binary_string;
}



