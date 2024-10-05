  var result = [];
  var current_max = numbers[0];

  for (const n of numbers) {
    if (n > current_max) {
      current_max = n;
    }
    result.push(current_max);
  }

  return result;
}



