  var result = [];
  var current_max = -Infinity;

  for (const n of numbers) {
    current_max = Math.max(n, current_max);
    result.push(current_max);
  }

  return result;
}



