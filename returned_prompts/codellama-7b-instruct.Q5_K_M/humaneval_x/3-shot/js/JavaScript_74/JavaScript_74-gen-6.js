  const len1 = lst1.join('').length;
  const len2 = lst2.join('').length;

  if (len1 < len2) {
    return lst1;
  } else if (len1 > len2) {
    return lst2;
  } else {
    return lst1;
  }
}



