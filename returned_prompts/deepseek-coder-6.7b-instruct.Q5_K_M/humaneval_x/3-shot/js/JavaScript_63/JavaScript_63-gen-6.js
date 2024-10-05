  if  (n === 0)  {
    return 0;
  } 
  if  (n === 1)  {
    return 0;
  } 
  if  (n === 2)  {
    return 1;
  } 

  let  prevPrev  = 0;
  let  prev  = 0;
  let  current  = 1;

  for  (let i = 3; i <= n; i++)  {
    let  temp  = current;
    current  += prev + prevPrev;
    prevPrev  = prev;
    prev  = temp;
  }

  return current;
}



