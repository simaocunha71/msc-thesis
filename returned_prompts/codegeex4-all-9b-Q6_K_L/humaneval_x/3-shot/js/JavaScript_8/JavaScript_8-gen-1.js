  if (numbers.length == 0) {
    return (0, 1);
  }
  var sum = 0;
  var product = 1;
  for (i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }
  return (sum, product);
}



