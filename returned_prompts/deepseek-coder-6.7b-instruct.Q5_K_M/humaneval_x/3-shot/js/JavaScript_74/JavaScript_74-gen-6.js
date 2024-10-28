  const totalChars 1  (lst)  (lst.reduce((acc, curr)  (acc  + curr.length), 0));
  const totalChars2  (lst2.reduce((acc, curr)  (acc  + curr.length), 0));
  return totalChars1 < totalChars2 ? lst1 : lst2;
}



