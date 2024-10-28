  var prime_digits = 0;
  for (const digit of num) {
    if (digit == 'A' || digit == 'B' || digit == 'D' || digit == 'E') {
      prime_digits += 1;
    }
  }
  return prime_digits;
}



