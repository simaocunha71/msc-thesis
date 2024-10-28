  let result = [0, 0];
  while (num > 0) {
    let digit = num % 10;
    if (digit % 2 == 0) {
      result[0] += 1;
    } else {
      result[1] += 1;
    }
    num = Math.floor(num / 10);
  }
  return result;
}



