  let sum1 = 0;
  let sum2 = 0;
  for (let i = 0; i < lst1.length; i++) {
    sum1 += lst1[i].length;
  }
  for (let j = 0; j < lst2.length; j++) {
    sum2 += lst2[j].length;
  }
  if (sum1 < sum2) {
    return lst1;
  } else {
    return lst2;
  }
}



