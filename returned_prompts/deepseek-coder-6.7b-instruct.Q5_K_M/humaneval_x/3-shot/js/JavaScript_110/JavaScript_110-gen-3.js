  let oddLst1 = lst1.filter(n => n % 2 !== 0);
  let evenLst2 = lst2.filter(n => n % 2 === 0);

  return oddLst1.length <= evenLst2.length ? "YES" : "NO";
}



