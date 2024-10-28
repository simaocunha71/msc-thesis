  let result = [];
  for (const digit of num.toString()) {
    if (digit % 2 == 0) {
      result[0] = result[0] + 1 || 1;
    } else {
      result[1] = result[1] + 1 || 1;
    }
  }
  return result;
}



