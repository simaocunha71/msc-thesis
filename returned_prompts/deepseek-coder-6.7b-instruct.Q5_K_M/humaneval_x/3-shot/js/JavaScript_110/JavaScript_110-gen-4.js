  let oddLst1 = lst1.filter(x => x % 2 != 0);
  let evenLst2 = lst2.filter(x => x % 2 == 0);

  return oddLst1.length <= evenLst2.length ? "YES" : "NO";
}



