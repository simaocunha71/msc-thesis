  let sum = 0;
  for (let n of lst) {
    sum += Math.pow(Math.ceil(n), 2);
  }
  return sum;
}