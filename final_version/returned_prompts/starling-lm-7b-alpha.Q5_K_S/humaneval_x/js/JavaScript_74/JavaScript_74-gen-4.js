  let total1 = lst1.reduce((acc, curr) => acc + curr.length, 0);
  let total2 = lst2.reduce((acc, curr) => acc + curr.length, 0);

  if (total1 < total2) {
    return lst1;
  } else if (total1 > total2) {
    return lst2;
  } else {
    return lst1;
  }
}



