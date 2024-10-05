const exchange = (lst1, lst2) => {
  let evenCount = 0;
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 === 0) {
      evenCount++;
    }
  }
  if (evenCount === lst1.length) {
    return "YES";
  }
  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 === 0) {
      evenCount--;
    }
  }
  if (evenCount === 0) {
    return "YES";
  }
  return "NO";
};
