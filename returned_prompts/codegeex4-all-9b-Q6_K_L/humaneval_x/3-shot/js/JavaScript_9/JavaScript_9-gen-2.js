  var result = [];
  var max = numbers[0];

  for (const n of numbers) {
    if (n > max) {
      max = n;
    }
    result.push(max);
  }

  return result;
}



