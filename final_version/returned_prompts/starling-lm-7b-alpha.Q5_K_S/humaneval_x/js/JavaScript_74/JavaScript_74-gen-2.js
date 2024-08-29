  let sum1 = 0;
  for (const str of lst1) {
    sum1 += str.length;
  }
  let sum2 = 0;
  for (const str of lst2) {
    sum2 += str.length;
  }
  if (sum1 < sum2) {
    return lst1;
  } else if (sum1 > sum2) {
    return lst2;
  } else {
    return lst1;
  }
}



