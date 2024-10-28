  var result = [];
  var count = {};

  for  (let num of numbers)  {
    if  (!count[num])  {
      count[num] = true;
      result.push(num);
    }
  }

  return result;
}



