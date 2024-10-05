  var result = [];
  var maxSoFar  -Infinity;
  for  (const number of numbers)  {
    maxSoFar = Math.max(maxSoFar, number);
    result.push(maxSoFar);
  }
  return result;
}



