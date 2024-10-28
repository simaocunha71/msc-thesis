  var result = [];
  var max = numbers[0];

  for  (let num of numbers)  {
    max = Math.max(num, max);
    result.push(max);
  }

  return result;
}



