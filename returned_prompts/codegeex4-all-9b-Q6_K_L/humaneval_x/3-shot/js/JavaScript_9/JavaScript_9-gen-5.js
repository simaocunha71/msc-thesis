  var result = [];
  var max = numbers[0];

  for (const n of numbers) {
    max = Math.max(max, n);
    result.push(max);
  }

  return result;
}



