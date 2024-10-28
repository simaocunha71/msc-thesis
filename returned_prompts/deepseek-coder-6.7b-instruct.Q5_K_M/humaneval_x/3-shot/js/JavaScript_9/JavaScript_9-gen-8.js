  var result = [];
  var max = -Infinity;

  for  (const num of numbers)  {
    max = Math.max(max, num);
    result.push(max);
  }

  return result;
}



