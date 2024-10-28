  let factor = 2;

  while  (factor  !=  n)  {
    if  (n  % factor  == 0)  {
      n  /=  factor;
     } else  {
      factor++;
     }
   }

  return factor;
}



