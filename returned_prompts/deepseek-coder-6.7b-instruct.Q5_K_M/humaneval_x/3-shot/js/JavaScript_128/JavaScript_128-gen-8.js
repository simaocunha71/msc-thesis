  if  (arr.length == 0)  {
    return null;
  }

  let sum = 0;
  let sign = 1;

  for  (let i  of arr)  {
    if  (i < 0)  {
      sign  *= -1;
      sum  -= Math.abs(i);
    } else if  (i > 0)  {
      sum  *= i;
    }
  }

  return sign * sum;
}



