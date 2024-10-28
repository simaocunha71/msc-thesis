  var count = { 0: 0, 1: 0 };
  var digits = Math.abs(num).toString().split("");
  for (const digit of digits) {
    if (digit % 2 == 0) {
      count[0] += 1;
    } else {
      count[1] += 1;
    }
  }
  return [count[0], count[1]];
}



