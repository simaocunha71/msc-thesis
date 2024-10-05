  if (arr.length == 0) {
    return null;
  }

  let prod = 1;
  let sum = 0;

  for (const num of arr) {
    prod *= Math.sign(num);
    sum += Math.abs(num);
  }

  return prod * sum;
}



