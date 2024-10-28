  let total_chars_1 = 0;
  let total_chars_2 = 0;

  for (const s of lst1) {
    total_chars_1 += s.length;
  }
  for (const s of lst2) {
    total_chars_2 += s.length;
  }

  if (total_chars_1 <= total_chars_2) {
    return lst1;
  } else {
    return lst2;
  }
}