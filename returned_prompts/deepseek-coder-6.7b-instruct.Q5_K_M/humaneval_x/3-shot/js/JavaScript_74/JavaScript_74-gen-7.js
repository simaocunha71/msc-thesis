  let sum1 = lst1.reduce((a, b) => a + b.length, 0);
  let sum2 = lst2.reduce((a, b) => a + b.length, 0);
  return sum1 < sum2 ? lst1 : lst2;
}



