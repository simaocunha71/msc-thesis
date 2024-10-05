  var result = 1;
  for (const digit of n.toString()) {
    if (digit % 2 == 1) {
      result *= digit;
    }
  }
  return result;
}