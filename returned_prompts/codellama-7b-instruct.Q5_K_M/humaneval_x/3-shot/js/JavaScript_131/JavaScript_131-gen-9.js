  var result = 1;
  for (const digit of n.toString()) {
    if (digit % 2 != 0) {
      result *= parseInt(digit);
    }
  }
  return result;
}



