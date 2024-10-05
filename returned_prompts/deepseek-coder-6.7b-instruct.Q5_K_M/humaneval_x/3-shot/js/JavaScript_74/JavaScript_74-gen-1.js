  const sum1 = lst1.reduce((acc, cur) => acc + cur.length, 0);
  const sum2 = lst2.reduce((acc, cur) => acc + cur.length, 0);
  return sum1 < sum2 ? lst1 : lst2;
}



