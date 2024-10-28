  var count_even = 0;
  var count_odd = 0;

  if (num < 0) {
    num = -num;
  }

  while (num > 0) {
    if ((num % 10) % 2 == 0) {
      count_even += 1;
    } else {
      count_odd += 1;
    }
    num = Math.floor(num / 10);
  }

  return [count_even, count_odd];
}