  let odd_count1 = 0;
  let odd_count2 = 0;
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 != 0) {
      odd_count1 += 1;
    }
  }
  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 != 0) {
      odd_count2 += 1;
    }
  }
  return odd_count1 <= odd_count2 ? "YES" : "NO";
}



