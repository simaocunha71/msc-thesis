  if  (n  <= 2)  {
    return 1;
  }

  let prev  = 1;
  let curr  = 1;

  for  (let  i  = 2; i  < n; i++)  {
    let  temp  =  curr;
    curr  +=  prev;
    prev  =  temp;
  }

  return curr;
}



