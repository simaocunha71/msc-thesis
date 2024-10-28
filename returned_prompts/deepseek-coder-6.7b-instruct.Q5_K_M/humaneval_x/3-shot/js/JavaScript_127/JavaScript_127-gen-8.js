  var start = Math.max(interval1[0], interval2[0]);
  var end = Math.min(interval1[1], interval2[1]);
  var length = end - start + 1;

  if  (length < 2)  {
    return "NO";
  }

  for  (let i = 2, sqrt = Math.sqrt(length); i <= sqrt; i++)  {
    if  (length % i === 0)  {
      return "NO";
    }
  }

  return "YES";
}



