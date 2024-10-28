  let factor = 2;

  while  (factor  * factor  le  n)  {
    if  (n  % factor  == 0)  {
      n  /=  factor;
    } else  {
      factor  +=  1;
    }
  }

  return n;
}



