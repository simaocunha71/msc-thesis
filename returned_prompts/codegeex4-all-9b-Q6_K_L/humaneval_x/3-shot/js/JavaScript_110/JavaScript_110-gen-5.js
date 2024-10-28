  var count1 = 0, count2 = 0;
  for (const i of lst1) {
    if (i % 2 == 1) {
      count1 += 1;
    }
  }
  for (const i of lst2) {
    if (i % 2 == 1) {
      count2 += 1;
    }
  }
  if (count1 <= count2) {
    return "YES";
  } else {
    return "NO";
  }
}