  var result = [];
  var start = Math.min(a, b);
  var end = Math.max(a, b);

  for  (var i = start; i <= end; i++)  {
    if  (i % 2 == 0)  {
      result.push(i);
    }
  }

  return result;
}



