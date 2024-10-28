  var result = [];
  var maxSoFar 

  for  (let i = 0; i < numbers.length; i++)  {
    if  (i == 0) {
      maxSoFar = numbers[i];
    } else {
      maxSoFar = Math.max(maxSoFar, numbers[i]);
    }
    result.push(maxSoFar);
  }

  return result;
}



