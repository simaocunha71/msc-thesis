  let count = 0;
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 == 0) {
      count += 1;
    }
  }

  if (count == lst1.length) {
    return "YES";
  }

  let odd_count = 0;
  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 == 1) {
      odd_count += 1;
    }
  }

  if (odd_count >= lst1.length - count) {
    return "YES";
  }

  return "NO";
}



