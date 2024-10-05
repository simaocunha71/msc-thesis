  var total1 = 0;
  var total2 = 0;

  for (const item of lst1) {
    total1 += item.length;
  }

  for (const item of lst2) {
    total2 += item.length;
  }

  if (total1 < total2) {
    return lst1;
  } else if (total1 > total2) {
    return lst2;
  } else {
    return lst1;
  }
}



