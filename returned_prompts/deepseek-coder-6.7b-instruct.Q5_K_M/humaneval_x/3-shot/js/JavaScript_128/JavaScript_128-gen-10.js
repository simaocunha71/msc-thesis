  if (arr.length === 0)  return null;

  let sum = 0;
  let prodSign = 1;

  for (let i = 0; i < arr.length; i++)  {
    let num = arr[i];
    if (num < 0)  {
      prodSign *= -1;
      num = -num;
    }  else if (num === 0)  {
      return 0;
    }
    sum += num;
  }

  return prodSign * sum;
}



