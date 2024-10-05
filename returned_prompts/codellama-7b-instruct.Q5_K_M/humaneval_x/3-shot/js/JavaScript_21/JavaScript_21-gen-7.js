  var min = Math.min.apply(null, numbers);
  var max = Math.max.apply(null, numbers);
  var range = max - min;

  var result = [];
  for (let n of numbers) {
    result.push((n - min) / range);
  }

  return result;
}



