  var maxes = [];
  var current_max = numbers[0];

  for  (const n of numbers)  {
    current_max = Math.max(current_max, n);
    maxes.push(current_max);
  }

  return maxes;
}



