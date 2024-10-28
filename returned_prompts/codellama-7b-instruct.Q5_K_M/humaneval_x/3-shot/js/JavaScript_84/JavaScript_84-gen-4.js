  var binary = (N >>> 0).toString(2);
  var sum = 0;

  for (const digit of binary) {
    sum += parseInt(digit);
  }

  return sum.toString(2);
}



