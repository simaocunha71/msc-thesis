  var collatz = [n];
  var current = n;

  while  (current  !=  1)  {
    current = current % 2  !=  0  ?  current * 3  +  1  :  current / 2;
    if  (current  %  2  !=  0)  {
      collatz.push(current);
    }
  }

  return collatz.sort((a, b) => a - b);
}



