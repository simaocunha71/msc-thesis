  var total_chars = 0;
  for (const s of lst1) {
    total_chars += s.length;
  }

  var other_total_chars = 0;
  for (const s of lst2) {
    other_total_chars += s.length;
  }

  if (total_chars < other_total_chars) {
    return lst1;
  } else if (total_chars > other_total_chars) {
    return lst2;
  } else {
    return lst1;
  }
}



