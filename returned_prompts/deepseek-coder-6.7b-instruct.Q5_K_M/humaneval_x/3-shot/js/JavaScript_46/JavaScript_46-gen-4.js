  if  (n  <= 2)  {
    return 0;
  } else if  (n  == 3)  {
    return 2;
  }

  let a  =  0;
  let b  =  0;
  let c  =  2;
  let d  =  a  +  b  +  c;

  for  (let i  =  4; i  <=  n; i++)  {
    let next  =  d;
    d  =  a  +  b  +  c  +  next;
    a  =  b;
    b  =  c;
    c  =  next;
  }

  return d;
}



