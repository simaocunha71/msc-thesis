  var sum = 0;
  var prod = 1;

  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    prod *= numbers[i];
  }

  return [sum, prod];
}



