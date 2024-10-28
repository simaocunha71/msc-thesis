  var sum = 0;
  var product = 1;
  for (var i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }
  return (sum, product);
}



