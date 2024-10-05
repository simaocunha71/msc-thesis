  const oddInLst1 = lst1.some(num => num % 2 !== 0);
  const oddInLst2 = lst2.some(num => num % 2 !== 0);

  if (!oddInLst1 && !oddInLst2) return "YES";
  if (oddInLst1 && oddInLst2) return "YES";

  return "NO";
}



