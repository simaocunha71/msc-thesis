  let result = [0, 0];
  let str = num.toString();
  for (let digit of str) {
    if (parseInt(digit) % 2 == 0) {
      result[0] += 1;
    } else {
      result[1] += 1;
    }
  }
  return result;
}



