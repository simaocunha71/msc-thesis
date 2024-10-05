  if  (n <= 2)  {
    return 1;
  }
  let prev  = 1, curr = 1;
  for  (let i = 3; i <= n; i++)  {
    let temp  = curr;
    curr  += prev;
    prev  = temp;
  }
  return curr;
}



