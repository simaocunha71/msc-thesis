  if (arr.length == 0) {
    return null;
  } else {
    var product = 1;
    var sum = 0;
    for (const i of arr) {
      product *= Math.sign(i);
      sum += Math.abs(i) * product;
    }
    return sum;
  }
}



