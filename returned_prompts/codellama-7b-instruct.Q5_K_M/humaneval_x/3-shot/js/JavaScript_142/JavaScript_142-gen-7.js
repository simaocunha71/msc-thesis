  var sum = 0;
  for (const i of lst) {
    if (i % 3 == 0) {
      sum += Math.pow(i, 2);
    } else if (i % 4 == 0) {
      sum += Math.pow(i, 3);
    }
  }
  return sum;
}



