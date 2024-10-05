  var even_count = 0;
  var odd_count = 0;

  while (num > 0) {
    if (num % 10 % 2 == 0) {
      even_count += 1;
    } else {
      odd_count += 1;
    }
    num = Math.floor(num / 10);
  }

  return [even_count, odd_count];
}



