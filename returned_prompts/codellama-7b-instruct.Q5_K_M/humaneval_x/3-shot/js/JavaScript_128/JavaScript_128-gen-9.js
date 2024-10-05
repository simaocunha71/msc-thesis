  if (arr.length == 0) {
    return null;
  }
  var product = 1;
  var sum = 0;

  for (const num of arr) {
    if (num > 0) {
      product *= 1;
      sum += num;
    } else if (num < 0) {
      product *= -1;
      sum += num;
    } else {
      sum += num;
    }
  }

  return product * sum;
}



