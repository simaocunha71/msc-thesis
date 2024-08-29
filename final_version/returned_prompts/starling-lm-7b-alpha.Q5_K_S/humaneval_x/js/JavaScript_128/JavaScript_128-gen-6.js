  if (arr.length === 0) {
    return null;
  }
  let sign = 1;
  let result = 0;
  for (const i of arr) {
    if (i === 0) {
      sign *= 0;
    } else if (i > 0) {
      sign *= 1;
    } else {
      sign *= -1;
    }
    result += Math.abs(i) * sign;
  }
  return result;
}



