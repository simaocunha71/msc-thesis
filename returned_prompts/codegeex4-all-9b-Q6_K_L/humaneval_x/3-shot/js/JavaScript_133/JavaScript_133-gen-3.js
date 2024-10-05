  var sum = 0;
  for (const num of lst) {
    sum += Math.pow(Math.ceil(num), 2);
  }
  return sum;
}

