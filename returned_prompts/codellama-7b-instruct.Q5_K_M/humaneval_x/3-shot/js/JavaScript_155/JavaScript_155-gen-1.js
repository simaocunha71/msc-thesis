  let even_count = 0;
  let odd_count = 0;

  while (num > 0) {
    let digit = num % 10;
    num = parseInt(num / 10);

    if (digit % 2 == 0) {
      even_count += 1;
    } else {
      odd_count += 1;
    }
  }

  return [even_count, odd_count];
}



