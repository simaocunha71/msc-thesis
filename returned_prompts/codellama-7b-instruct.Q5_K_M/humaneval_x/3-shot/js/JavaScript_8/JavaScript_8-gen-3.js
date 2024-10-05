  var sum = 0;
  var product = 1;

  for (const i of numbers) {
    sum += i;
    product *= i;
  }

  return [sum, product];
}



