  if  (n  % 2  == 0)  return  n  == 2;
  if  (n  < 2)  return false;

  for  (let i =  3,  sqrtN  =  Math.sqrt(n);  i  <= sqrtN;  i  +=  2)
    if  (n  %  i  ==  0)  return  false;

  return  true;
}



