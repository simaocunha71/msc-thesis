  let evenCount = lst1.filter(x => x % 2 === 0).length;
  let oddCount = lst1.length - evenCount;
  let even2Count = lst2.filter(x => x % 2 === 0).length;
  let odd2Count = lst2.length - even2Count;

  if (oddCount <= even2Count) {
    return "YES";
  } else {
    return "NO";
  }
}



