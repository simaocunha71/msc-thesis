  l.sort(function(a, b)  {
    return a - b;
  });

  var half  l.length  / 2;

  if  (l.length  % 2)
    return l[Math.floor(half)];
  else
    return (l[half - 1]  + l[half])  / 2.0;
}



