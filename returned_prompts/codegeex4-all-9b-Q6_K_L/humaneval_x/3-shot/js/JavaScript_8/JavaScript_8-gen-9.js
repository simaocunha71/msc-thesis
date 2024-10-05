  var sum = 0;
  var product = 1;

  if (numbers.length == 0) {
    return (sum, product);
  }
  for (const n of numbers) {
    sum += n;
    product *= n;
  }
  return (sum, product);
}



