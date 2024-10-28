  var count = [0, 0];
  for (const digit of Math.abs(num).toString()) {
    if (digit % 2 == 0) {
      count[0] += 1;
    } else {
      count[1] += 1;
    }
  }
  return count;
}



