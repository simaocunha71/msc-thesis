  var result = [];
  var max = -Infinity;

  for  (const number of numbers)  {
    max = Math.max(max, number);
    result.push(max);
  }

  return result;
}



