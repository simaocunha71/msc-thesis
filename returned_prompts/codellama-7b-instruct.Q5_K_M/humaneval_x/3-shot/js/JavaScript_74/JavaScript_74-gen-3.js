  var total_chars_lst1 = 0;
  var total_chars_lst2 = 0;
  var total_chars_smaller_lst1 = 0;

  for (const s of lst1) {
    total_chars_lst1 += s.length;
  }

  for (const s of lst2) {
    total_chars_lst2 += s.length;
  }

  for (const s of lst1) {
    if (s.length < total_chars_lst2) {
      total_chars_smaller_lst1 += s.length;
    }
  }

  if (total_chars_smaller_lst1 < (total_chars_lst2 - total_chars_lst1)) {
    return lst1;
  } else if (total_chars_smaller_lst1 == (total_chars_lst2 - total_chars_lst1)) {
    return lst1;
  } else {
    return lst2;
  }
}



