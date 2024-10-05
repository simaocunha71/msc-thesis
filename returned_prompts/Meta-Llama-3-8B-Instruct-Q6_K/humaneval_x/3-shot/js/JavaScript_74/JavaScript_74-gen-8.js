  let sum1 = 0, sum2 = 0;
  for (let i = 0; i < lst1.length; i++) {
    sum1 += lst1[i].length;
  }
  for (let i = 0; i < lst2.length; i++) {
    sum2 += lst2[i].length;
  }
  if (sum1 < sum2) {
    return lst1;
  } else if (sum1 > sum2) {
    return lst2;
  } else {
    return lst1;
  }
}