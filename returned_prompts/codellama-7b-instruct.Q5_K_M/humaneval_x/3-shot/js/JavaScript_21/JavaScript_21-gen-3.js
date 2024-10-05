  var min = Math.min(...numbers);
  var max = Math.max(...numbers);
  var diff = max - min;
  var result = [];

  for (const num of numbers) {
    result.push((num - min) / diff);
  }

  return result;
}



