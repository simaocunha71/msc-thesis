  var result = [];
  var max_so_far = numbers[0];

  for  (let num of numbers)  {
    max_so_far = Math.max(max_so_far, num);
    result.push(max_so_far);
  }

  return result;
}



