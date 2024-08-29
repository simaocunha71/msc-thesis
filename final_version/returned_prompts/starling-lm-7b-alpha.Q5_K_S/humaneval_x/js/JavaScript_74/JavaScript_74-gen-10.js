  let total_char1 = 0;
  let total_char2 = 0;
  let result = [];

  for (const s of lst1) {
    total_char1 += s.length;
  }

  for (const s of lst2) {
    total_char2 += s.length;
  }

  if (total_char1 < total_char2) {
    result = lst1;
  } else if (total_char1 > total_char2) {
    result = lst2;
  } else {
    result = lst1;
  }

  return result;
}



