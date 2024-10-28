  var result = [];
  var max = -Infinity;

  for (const n of numbers) {
    if (n > max) {
      max = n;
    }
    result.push(max);
  }

  return result;
}