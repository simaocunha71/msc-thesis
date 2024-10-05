  let total_chars1 = 0;
  for (const s of lst1) {
    total_chars1 += s.length;
  }
  let total_chars2 = 0;
  for (const s of lst2) {
    total_chars2 += s.length;
  }

  if (total_chars1 <= total_chars2) {
    return lst1;
  } else {
    return lst2;
  }
}



