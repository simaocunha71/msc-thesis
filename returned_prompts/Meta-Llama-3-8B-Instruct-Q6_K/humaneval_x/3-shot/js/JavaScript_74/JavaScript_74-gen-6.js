  let total1 = 0, total2 = 0;

  for (let i = 0; i < lst1.length; i++) {
    total1 += lst1[i].length;
  }

  for (let i = 0; i < lst2.length; i++) {
    total2 += lst2[i].length;
  }

  if (total1 < total2) {
    return lst1;
  } else if (total1 > total2) {
    return lst2;
  } else {
    return lst1;
  }
}