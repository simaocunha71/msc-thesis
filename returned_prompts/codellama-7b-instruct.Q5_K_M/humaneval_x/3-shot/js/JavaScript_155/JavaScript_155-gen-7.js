  var even_count = 0;
  var odd_count = 0;

  while (num > 0) {
    var last_digit = num % 10;
    if (last_digit % 2 == 0) {
      even_count += 1;
    } else {
      odd_count += 1;
    }
    num /= 10;
  }

  return [even_count, odd_count];
}



