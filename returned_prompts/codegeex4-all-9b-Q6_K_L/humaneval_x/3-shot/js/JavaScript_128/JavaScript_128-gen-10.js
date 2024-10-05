  if (arr.length == 0) {
    return null;
  }
  var prod = 1;
  var sum = 0;
  for (const num of arr) {
    prod *= Math.sign(num);
    sum += Math.abs(num);
  }
  return prod * sum;
}