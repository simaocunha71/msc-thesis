  let numStr = String(Math.abs(num));
  let result = [0, 0];
  for (const digit of numStr) {
    result[digit % 2] += 1;
  }
  return result;
}



