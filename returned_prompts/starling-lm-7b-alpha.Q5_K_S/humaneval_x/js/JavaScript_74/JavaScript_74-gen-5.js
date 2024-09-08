  let total_chars = lst1.reduce((acc, curr) => acc + curr.length, 0);
  let total_chars2 = lst2.reduce((acc, curr) => acc + curr.length, 0);
  if (total_chars < total_chars2) {
    return lst1;
  } else if (total_chars > total_chars2) {
    return lst2;
  } else {
    return lst1;
  }
}



