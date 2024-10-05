  let result = 1;

  for  (let i = n; i > 0; i--)  {
    let factorial_i =  1;
    for  (let j = i; j > 0; j--)  {
      factorial_i *= j;
    }
    result *= factorial_i;
  }

  return result;
}



