  let sum1 = 0, sum2 = 0;
  for (let i = 0; i < lst1.length; i++) {
    sum1 += lst1[i];
  }
  for (let i = 0; i < lst2.length; i++) {
    sum2 += lst2[i];
  }
  if (sum1 % 2 == 0 && sum2 % 2 == 0) {
    for (let i = 0; i < lst1.length; i++) {
      if (lst1[i] % 2 != 0) {
        for (let j = 0; j < lst2.length; j++) {
          if (lst2[j] % 2 == 0) {
            [lst1[i], lst2[j]] = [lst2[j], lst1[i]];
            break;
          }
        }
      }
    }
    for (let i = 0; i < lst1.length; i++) {
      if (lst1[i] % 2 != 0) {
        return "NO";
      }
    }
    return "YES";
  }
  return "NO";
}



