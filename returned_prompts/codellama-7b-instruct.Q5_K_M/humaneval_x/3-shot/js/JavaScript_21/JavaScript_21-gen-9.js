  var min = Math.min(...numbers);
  var max = Math.max(...numbers);
  var range = max - min;
  var result = numbers.map(x => (x - min) / range);
  return result;
}



