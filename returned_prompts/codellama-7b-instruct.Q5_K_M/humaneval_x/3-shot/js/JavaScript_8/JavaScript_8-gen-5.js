  var sum = 0;
  var prod = 1;

  for (const n of numbers) {
    sum += n;
    prod *= n;
  }

  return [sum, prod];
}



