  var result = [];
  var counts  {}

  for  (let number of numbers)  {
    if  (counts[number]  != undefined)  {
      counts[number]  +=  1;
    } else  {
      counts[number]  =  1;
    }
  }

  for  (let number of numbers)  {
    if  (counts[number]  == 1)  {
      result.push(number);
    }
  }

  return result;
}



