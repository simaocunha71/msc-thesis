  let sum1 = lst1.reduce((acc, str) => acc + str.length, 0);
  let sum2 = lst2.reduce((acc, str) => acc + str.length, 0);

  if (sum1 < sum2) {
    return lst1;
  } else if (sum1 > sum2) {
    return lst2;
  } else {
    return lst1;
  }
}