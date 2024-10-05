  let totalCharLst1 = 0;
  let totalCharLst2 = 0;

  for (const str of lst1) {
    totalCharLst1 += str.length;
  }

  for (const str of lst2) {
    totalCharLst2 += str.length;
  }

  if (totalCharLst1 < totalCharLst2) {
    return lst1;
  } else if (totalCharLst1 > totalCharLst2) {
    return lst2;
  } else {
    return lst1;
  }
}



