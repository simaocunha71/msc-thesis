  let evens = 0;
  let odds = 0;
  while (num > 0) {
    if (num % 2 == 0) {
      evens += 1;
    } else {
      odds += 1;
    }
    num = Math.floor(num / 10);
  }
  return [evens, odds];
}



