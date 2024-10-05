  var result = [];
  var currentMax = numbers[0];

  for  (let number of numbers) {
    currentMax = Math.max(currentMax, number);
    result.push(currentMax);
  }

  return result;
}



