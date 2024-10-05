  if (lst1.length == 0 || lst2.length == 0) {
    return "NO";
  }

  var lst1_even_count = 0;
  var lst2_even_count = 0;

  for (const el of lst1) {
    if (el % 2 == 0) {
      lst1_even_count += 1;
    }
  }

  for (const el of lst2) {
    if (el % 2 == 0) {
      lst2_even_count += 1;
    }
  }

  return (lst1_even_count > 0 && lst2_even_count > 0) ? "YES" : "NO";
}



