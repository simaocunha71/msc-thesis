  if (arr.length === 0)  { return null; }

  let sum = 0;
  let sign = 1;

  for (let num of arr) {
    if (num < 0) {
      sign *= -1;
      num = Math.abs(num);
    } else if (num === 0) {
      return 0;
    }
    sum += num;
  }

  return sign * sum;
}



