  if (numbers.length == 0) {
    return (0, 1);
  }
  else {
    var sum = 0;
    var product = 1;

    for (const num of numbers) {
      sum += num;
      product *= num;
    }

    return (sum, product);
  }
}



