  var countEven = 0, countOdd = 0;
  while (num > 0) {
    if (num % 10 % 2 == 0) countEven++;
    else countOdd++;
    num = Math.floor(num / 10);
  }
  return [countEven, countOdd];
}



