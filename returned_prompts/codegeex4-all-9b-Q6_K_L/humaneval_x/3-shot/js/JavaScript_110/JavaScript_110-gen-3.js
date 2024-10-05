  var even_count = 0;
  for (const c of lst1) {
    if (c % 2 == 0) {
      even_count += 1;
    }
  }
  for (const c of lst2) {
    if (c % 2 == 0) {
      even_count += 1;
    }
  }
  if (even_count >= lst1.length) {
    return "YES";
  } else {
    return "NO";
  }
}