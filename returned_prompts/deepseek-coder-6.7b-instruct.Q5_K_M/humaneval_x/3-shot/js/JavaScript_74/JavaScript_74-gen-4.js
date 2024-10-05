  let sum1 = 0;
  let sum2 = 0;

  for  (let i  of lst1)  {
    sum1 += i.length;
  }

  for  (let j  of lst2)  {
    sum2 += j.length;
  }

  return sum1 < sum2 ? lst1 : lst2;
}



