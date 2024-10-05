  let sum = 0;

  for (let num of lst) {
    sum += Math.ceil(num) ** 2;
  }

  return sum;
}

