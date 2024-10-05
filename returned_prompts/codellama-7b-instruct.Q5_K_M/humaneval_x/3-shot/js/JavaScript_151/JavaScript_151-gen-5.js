  var sum = 0;

  for (const i of lst) {
    if (i % 1 == 0 && i > 0) {
      sum += Math.pow(i, 2);
    }
  }

  return sum;
}



