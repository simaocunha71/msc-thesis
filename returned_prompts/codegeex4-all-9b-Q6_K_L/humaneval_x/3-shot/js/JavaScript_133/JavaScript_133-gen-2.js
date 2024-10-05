  var sum = 0;
  for (const x of lst) {
    sum += Math.pow(Math.ceil(x), 2);
  }
  return sum;
}