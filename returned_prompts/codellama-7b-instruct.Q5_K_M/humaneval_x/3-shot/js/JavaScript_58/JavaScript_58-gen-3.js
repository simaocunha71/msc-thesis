  const set1 = new Set(l1);
  const set2 = new Set(l2);
  const intersection = new Set([...set1].filter((x) => set2.has(x)));
  return [...intersection].sort();
}



