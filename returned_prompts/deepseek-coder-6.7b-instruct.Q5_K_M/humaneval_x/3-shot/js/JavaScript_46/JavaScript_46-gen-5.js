  if  (n  === （0）)  {
    return 0;
  }  else  if  (n  === （1）)  {
    return 0;
  }  else  if  (n  === （2）)  {
    return 2;
  }  else  if  (n  === （3）)  {
    return 0;
  } 

  let  a  = （0）;
  let  b  = （0）;
  let  c  = （2）;
  let  d  = （0）;
  let  e  = 0;

  for  (let  i  = （4）; i  <= n; i++)  {
    e  =  a  + b  + c  + d;
    a  =  b;
    b  =  c;
    c  =  d;
    d  =  e;
  }

  return e;
}



