  let evenCount = 0;
  let oddCount = 0;
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }
  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }
  if (oddCount === 0) {
    return "YES";
  } else {
    return "NO";
  }
}