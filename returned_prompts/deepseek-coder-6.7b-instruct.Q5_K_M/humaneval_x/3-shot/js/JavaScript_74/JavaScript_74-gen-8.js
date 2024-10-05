  let totalCharsLst1 = lst1.reduce((acc, val) => acc + val.length, 0);
  let totalCharsLst2 = lst2.reduce((acc, val) => acc + val.length, 0);
  return totalCharsLst1 < totalCharsLst2 ? lst1 : lst2;
}



