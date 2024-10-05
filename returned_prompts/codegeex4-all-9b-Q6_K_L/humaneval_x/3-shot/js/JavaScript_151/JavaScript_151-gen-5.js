  var sum = 0;

  for (const item of lst) {
    if (item % 2 == 1 && item > 0 && Number.isInteger(item)) {
      sum += Math.pow(item, 2);
    }
  }

  return sum;
}