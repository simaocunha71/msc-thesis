  if  (n  <  2)  {
    return 0;
  } else if  (n  ==  2)  {
    return 1;
  }

  let  prev_prev  = 0;
  let  prev  = 0;
  let  current  = 1;

  for  (let  i  =  2; i  <  n; i++)  {
    let  temp  =  current;
    current  +=  prev  +  prev_prev;
    prev_prev  =  prev;
    prev  =  temp;
  }

  return  current;
}



