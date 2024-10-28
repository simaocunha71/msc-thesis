  var maxStart 
  = Math.max(interval1[0], interval2[0]);
  var minEnd 
  = Math.min(interval1[1], interval2[1]);

  if  (maxStart > minEnd) 
  {
    return "NO";
  }

  var length 
  = minEnd - maxStart;

  if  (length < 2) 
  {
    return "NO";
  }

  for  (var i = 2; i * i <= length; i++) 
  {
    if  (length % i === 0) 
    {
      return "NO";
    }
  }

  return "YES";
}



