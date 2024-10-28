  let total1 = 0;
  let total2 = 0;

  for (const s of lst1) {
    total1 += s.length;
  }
  for (const s of lst2) {
    total2 += s.length;
  }

  if (total1 <= total2) {
    return lst1;
  } else {
    return lst2;
  }
}