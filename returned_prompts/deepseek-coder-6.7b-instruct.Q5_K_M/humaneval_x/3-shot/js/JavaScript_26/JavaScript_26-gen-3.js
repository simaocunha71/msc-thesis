  var result = [];
  var counts = {};

  for  (let n of numbers) {
    if  (counts[n]  != undefined) {
      counts[n]  +=  1;
    } else {
      counts[n]  =  1;
    }
  }

  for  (let n of numbers) {
    if  (counts[n]  == 1) {
      result.push(n);
    } else {
      counts[n]  -=  1;
    }
  }

  return result;
}



