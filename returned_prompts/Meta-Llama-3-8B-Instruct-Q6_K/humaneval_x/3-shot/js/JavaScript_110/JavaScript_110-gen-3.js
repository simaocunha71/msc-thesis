  let evenCount = 0;
  for (let num of lst1) {
    if (num % 2 == 0) {
      evenCount++;
    }
  }
  for (let num of lst2) {
    if (num % 2 == 0) {
      evenCount++;
    }
  }
  return evenCount >= lst1.length;
}