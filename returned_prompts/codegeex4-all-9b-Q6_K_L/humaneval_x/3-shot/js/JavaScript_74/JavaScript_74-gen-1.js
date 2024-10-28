  const totalChars = (lst) => {
    let total = 0;
    for (const word of lst) {
      total += word.length;
    }
    return total;
  }

  let total1 = totalChars(lst1);
  let total2 = totalChars(lst2);

  if (total1 < total2) {
    return lst1;
  } else if (total2 < total1) {
    return lst2;
  } else {
    return lst1;
  }
}