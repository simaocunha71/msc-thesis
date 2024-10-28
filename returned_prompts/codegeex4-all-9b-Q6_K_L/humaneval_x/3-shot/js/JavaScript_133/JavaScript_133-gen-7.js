  var sum = 0;
  for (const item of lst) {
    sum += Math.pow(Math.ceil(item), 2);
  }
  return sum;
}