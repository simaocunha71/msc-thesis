  let odd_count = 0;
  for (const i of lst1) {
    if (i % 2 == 0) {
    } else {
      odd_count += 1;
    }
  }
  if (odd_count == 0) {
    return "YES";
  }
  let odd_count2 = 0;
  for (const i of lst2) {
    if (i % 2 == 0) {
    } else {
      odd_count2 += 1;
    }
  }
  return odd_count2 >= odd_count ? "YES" : "NO";
}



