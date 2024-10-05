  var result = [];

  if  (a > b)  {
    var temp = a;
    a = b;
    b = temp;
  }

  for  (let i = a; i <= b; i++)  {
    if  (i % 2 == 0)  {
      result.push(i);
    }
  }

  return result;
}



