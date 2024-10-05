  let sum1 = 0;
  let sum2 = 0;
  for (const s of lst1) {
    sum1 += s.length;
  }
  for (const s of lst2) {
    sum2 += s.length;
  }

  if (sum1 < sum2) {
    return lst1;
  } else if (sum1 > sum2) {
    return lst2;
  } else {
    return lst1;
  }
}