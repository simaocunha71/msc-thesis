  var result = [];
  var max = numbers[0];

  for  (let number of numbers)  {
    max = Math.max(max, number);
    result.push(max);
  }

  return result;
}



