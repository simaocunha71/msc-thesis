  if (arr.length === 0) {
    return null;
  }

  let sign = 1;
  let result = 0;

  for (const num of arr) {
    if (num < 0) {
      sign *= -1;
    } else if (num > 0) {
      sign *= 1;
    } else {
      sign *= 0;
    }
    result += sign * Math.abs(num);
  }

  return result;
}



