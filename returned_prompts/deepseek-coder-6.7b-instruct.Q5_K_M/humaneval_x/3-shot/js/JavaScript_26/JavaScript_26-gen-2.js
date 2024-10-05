  var result = [];
  var counts = {};

  for  (const n of numbers)  {
    if  (counts[n])  {
      counts[n] += 1;
    } else  {
      counts[n] = 1;
    }
  }

  for  (const n of numbers)  {
    if  (counts[n] == 1)  {
      result.push(n);
    }
  }

  return result;
}



