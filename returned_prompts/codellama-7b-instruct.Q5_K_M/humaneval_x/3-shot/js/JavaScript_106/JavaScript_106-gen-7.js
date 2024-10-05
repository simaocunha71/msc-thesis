  var result = [];

  for (let i = 0; i < n; i++) {
    if (i % 2 == 0) {
      result.push(i * factorial(i));
    } else {
      result.push(sum_numbers(i));
    }
  }

  return result;
}



