  let sum1 = 0;
  let sum2 = 0;

  for (let str of lst1) {
    sum1 += str.length;
  }

  for (let str of lst2) {
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
//Note: The above function will return the first list if both lists have the same number of chars, as per the problem statement. If you want to return both lists in this case, you can modify the function accordingly.