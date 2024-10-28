  var even_count = 0;
  var odd_count = 0;
  for (const digit of String(Math.abs(num))) {
    if (parseInt(digit) % 2 == 0) {
      even_count += 1;
    } else {
      odd_count += 1;
    }
  }
  return [even_count, odd_count];
}



