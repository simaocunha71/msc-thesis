  var result = [];
  var current_max = numbers[0];

  for (const n of numbers) {
    current_max = Math.max(n, current_max);
    result.push(current_max);
  }

  return result;
}



