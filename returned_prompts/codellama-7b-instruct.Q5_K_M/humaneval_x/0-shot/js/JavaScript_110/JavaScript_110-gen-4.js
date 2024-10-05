const exchange = (lst1, lst2) => {
  // make a copy of the lists
  const copyLst1 = [...lst1];
  const copyLst2 = [...lst2];

  // make a set of all the even numbers in the second list
  const evenNumbers = new Set();
  for (let i = 0; i < copyLst2.length; i++) {
    if (copyLst2[i] % 2 === 0) {
      evenNumbers.add(copyLst2[i]);
    }
  }

  // check if any element in the first list is not even
  for (let i = 0; i < copyLst1.length; i++) {
    if (!evenNumbers.has(copyLst1[i])) {
      return "NO";
    }
  }
  return "YES";
}

