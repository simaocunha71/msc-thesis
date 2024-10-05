  var result = [];
  var current_max = -Infinity;

  for (const n of numbers) {
    current_max = Math.max(current_max, n);
    result.push(current_max);
  }

  return result;
}



